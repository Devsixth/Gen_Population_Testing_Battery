import sqlite3
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC
from business_rules.variables import BaseVariables, numeric_rule_variable
import plotly.graph_objects as go
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.platypus.frames import Frame
from reportlab.lib.enums import TA_CENTER

def get_recommendation(fq):
    if fq == 'VERY GOOD':
        return "The Assessment results show a high Fitness Quotient indicating better Quality of Life which results in reduced susceptibility to injuries and ability to perform routine activities with minimal pain to no pain. Stay physically active to maintain the same."
    elif fq == 'GOOD':
        return "The Assessment results demonstrate a good Fitness Quotient, reflecting a satisfactory level of quality of life. There are areas for improvement that can reduce the susceptibility of injury occurrence and optimise your Fitness Quotient. Consult with an Exercise Scientist."
    elif fq == 'MODERATE':
        return "The Assessment indicates a moderate Fitness Quotient, highlighting potential injury risks and physical discomfort. Urgent intervention is necessary to mitigate these risks effectively."
    elif fq == 'POOR':
        return "The Assessment results indicate a concerning decrease in the Fitness Quotient, signifying an elevated risk of injury and a notable deterioration in quality of life. Immediate attention and intervention are essential."
    elif fq == 'VERY POOR':
        return "The Assessment results reveal a significantly deficient Fitness Quotient, suggesting an increased risk of injury and a notable compromise in quality of life. Immediate attention and intervention are warranted."
    else:
        return "Fitness Quotient calculation unknown."

class FQCalculator:
    def __init__(self, AA, A, BA):
        self.AA = AA
        self.A = A
        self.BA = BA

    def fq_string(self):
        if self.AA == 6 or self.AA == 5:
            return 'VERY GOOD'
        elif self.AA == 4 or (self.AA == 3 and self.A > 0):
            return 'GOOD'
        elif (self.AA == 3 and self.A == 0) or \
             (self.AA == 2) or \
             (self.AA == 1 and self.BA == 0):
            return 'MODERATE'
        elif (self.AA == 1 and self.BA > 0) or \
             (self.AA == 0 and self.A > 1):
            return 'POOR'
        elif self.AA == 0 and self.A <= 1:
            return 'VERY POOR'
        else:
            return 'UNKNOWN'

class GradeCalculator(BaseActions):
    GRADE_MAPPING = {
        'VERY POOR': 1,
        'POOR': 2,
        'MODERATE': 3,
        'GOOD': 4,
        'VERY GOOD': 5
    }

    def __init__(self, fq_value):
        self.grade = self.GRADE_MAPPING.get(fq_value, 0)

    @rule_action(params={"grade": FIELD_NUMERIC})
    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

class DataVariables(BaseVariables):
    def __init__(self, fq_value):
        self.fq_value = fq_value

    @numeric_rule_variable
    def fq_numeric(self):
        return GradeCalculator(self.fq_value).get_grade()

def calculate_fq(AA, A, BA):
    fq_calculator = FQCalculator(AA, A, BA)
    return fq_calculator.fq_string()

def check_fq_grade(fq_value):
    variables = DataVariables(fq_value)
    actions = GradeCalculator(fq_value)
    run_all(rule_list=[], defined_variables=variables, defined_actions=actions)
    return actions.get_grade()

def load_data_from_db(db_file, client_id, date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Fetch client data
    client_query = "SELECT * FROM ClientDetails WHERE clientid = ?"
    cursor.execute(client_query, (client_id,))
    client_data = cursor.fetchone()
    client_columns = [description[0] for description in cursor.description]

    if not client_data:
        print(f"No data found for clientid: {client_id} on date: {date}")
        conn.close()
        return None

    client_data = dict(zip(client_columns, client_data))

    # Fetch test data for the current client
    test_query = "SELECT testname, status FROM test_details WHERE clientid = ? AND date = ?"
    cursor.execute(test_query, (client_id, date))
    test_rows = cursor.fetchall()
    test_columns = [description[0] for description in cursor.description]

    test_data = [dict(zip(test_columns, test_row)) for test_row in test_rows]
    client_data['Tests'] = test_data

    # Fetch recommendations data
    recommendations_query = "SELECT test_name, status, recommendation FROM recommendationdetails"
    cursor.execute(recommendations_query)
    recommendations_data = cursor.fetchall()
    recommendations_dict = {(row[0], row[1].lower()): row[2] for row in recommendations_data}

    # Debug: Print fetched recommendations
    #print("Fetched Recommendations:", recommendations_dict)

    # Count the statuses and add recommendations
    status_counts = {'above average': 0, 'average': 0, 'below average': 0}
    for test in test_data:
        status = test['status'].lower()
        if status in status_counts:
            status_counts[status] += 1
        # Add recommendations if status is "above average", "average" or "below average"
        test['recommendation'] = recommendations_dict.get((test['testname'], status), '')

    # Debug: Print test data with recommendations
    #print("Test Data with Recommendations:", test_data)

    # Calculate FQ and FQ_Numeric
    client_data['AA'] = status_counts['above average']
    client_data['A'] = status_counts['average']
    client_data['BA'] = status_counts['below average']
    client_data['FQ'] = calculate_fq(client_data['AA'], client_data['A'], client_data['BA'])
    client_data['FQ_Numeric'] = check_fq_grade(client_data['FQ'])

    conn.close()
    return client_data

def create_gauge(fq_numeric, output_path):
    plot_bgcolor = "#ffffff"
    quadrant_colors = [plot_bgcolor, "#2bad4e", "#85e043", "#eff229", "#f2a529", "#f25829"]
    quadrant_text = ["", "<b>Very Good</b>", "<b>Good</b>", "<b>Moderate</b>", "<b>Poor</b>", "<b>Very Poor</b>"]
    n_quadrants = len(quadrant_colors) - 1

    min_value = 0
    max_value = 5
    hand_length = np.sqrt(2) / 4
    hand_angle = np.pi * (1 - (max(min_value, min(max_value, fq_numeric)) - min_value) / (max_value - min_value))

    fig = go.Figure(
        data=[
            go.Pie(
                values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
                rotation=90,
                hole=0.5,
                marker_colors=quadrant_colors,
                text=quadrant_text,
                textinfo="text",
                hoverinfo="skip",
                textfont=dict(size=30)  # Increase the font size of the quadrant text
            ),
        ],
        layout=go.Layout(
            showlegend=False,
            margin=dict(b=0, t=10, l=10, r=10),
            width=1500,  # Increased width
            height=1500,  # Increased height
            paper_bgcolor=plot_bgcolor,
            annotations=[
                go.layout.Annotation(
                    text=f"<b>Fitness Quotient:</b><br>{fq_numeric}",
                    x=0.5, xanchor="center", xref="paper",
                    y=0.20, yanchor="bottom", yref="paper",  # Adjusted y position for better alignment
                    showarrow=False,
                    font=dict(size=90)  # Increased font size for better readability
                )
            ],
            shapes=[
                go.layout.Shape(
                    type="line",
                    x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                    y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                    line=dict(color="#333", width=4)  # Increased line width for better visibility
                )
            ]
        )
    )
    fig.write_image(output_path)

def create_pdf(data):
    pdf_file = f"Assessment_Report_{data['clientid']}_{data['date']}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    styles = getSampleStyleSheet()

    # Title and image
    c.setFont("Helvetica-Bold", 18)
    title_x = 50
    title_y = height - 80
    c.setFillColor(colors.midnightblue)
    c.drawString(title_x, title_y, "Comprehensive Physical Assessment")

    image_path = "C:/Users/Admin/Desktop/gen/images/Logo.jpg"
    image_x = title_x + 370
    image_y = title_y - 25
    c.drawImage(image_path, image_x, image_y, width=80, height=80)

    # Draw a line after the title and image
    line_y = title_y - 35
    c.setStrokeColor(colors.midnightblue)
    c.setLineWidth(1)
    c.line(title_x, line_y, width - title_x, line_y)

    # Personal details
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    details_y = title_y - 50
    c.drawString(50, details_y, f"Name: {data['name']}")
    c.drawString(50, details_y - 20, f"Gender: {data['gender']}")
    c.drawString(350, details_y, f"Date of Birth: {data['dob']}")
    c.drawString(350, details_y - 20, f"Date: {data['date']}")

    # Subtitle for Assessment Results
    c.setFillColor(colors.purple)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, details_y - 40, "Assessment Results")

    # Table for Assessment Results
    results_y = details_y - 200
    test_data = [
        ["Test Name", "Status"]
    ]
    for test in data['Tests']:
        test_data.append([test['testname'], test['status']])

    table = Table(test_data, colWidths=[200, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.rosybrown),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, results_y)
    # Subtitle for Fitness Quotient
    fq_y = results_y - 50
    c.setFillColor(colors.darkblue)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, fq_y, "Fitness Quotient")
    c.setFont("Helvetica", 8)
    c.drawString(50, fq_y - 15, f"{data['FQ']}")

    # Gauge plot
    gauge_image_path = "gauge_plot.png"
    create_gauge(data['FQ_Numeric'], gauge_image_path)
    c.drawImage(gauge_image_path, 50, fq_y - 300, width=250, height=250)

    # Recommendation text
    recommendation_text = get_recommendation(data['FQ'])
    style = ParagraphStyle(
        name='Normal',
        fontSize=12,
        leading=20,
        spaceAfter=10,
        alignment=TA_CENTER  # Center align the text
    )
    recommendation_paragraph = Paragraph(recommendation_text, style)
    frame = Frame(320, fq_y - 300, 200, 250, showBoundary=0)
    frame.addFromList([recommendation_paragraph], c)

    # Referral Statement
    ref_y = fq_y - 330
    c.setFillColor(colors.darkblue)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, ref_y, "Referral Statement")
    c.setFont("Helvetica", 10)
    ref_text = Paragraph(data['Referral_Statement'], styles['Normal'])
    ref_text.wrap(500, 400)
    ref_text.drawOn(c, 50, ref_y - 30)
    c.showPage()
    # Title and image for the second page
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.midnightblue)
    c.drawString(title_x, title_y, "Comprehensive Physical Assessment")

    c.drawImage(image_path, image_x, image_y, width=80, height=80)

    c.setStrokeColor(colors.midnightblue)
    c.setLineWidth(1)
    c.line(title_x, line_y, width - title_x, line_y)

    # Personal details
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    details_y = title_y - 50
    c.drawString(50, details_y, f"Name: {data['name']}")
    c.drawString(50, details_y - 20, f"Gender: {data['gender']}")
    c.drawString(350, details_y, f"Date of Birth: {data['dob']}")
    c.drawString(350, details_y - 20, f"Date: {data['date']}")


    # Subtitle for Recommendations
    rec1_y = details_y - 40  # Adjust starting Y position for recommendations section

    c.setFillColor(colors.olivedrab)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, rec1_y, "Recommendations")

    # Fixed space between the title and the table
    space_between_title_and_table = 7  # Adjust this value as needed

    # Calculate the starting position for the recommendations table
    table_start_y = rec1_y - space_between_title_and_table  # Ensure it starts just below the title

    # Recommendations Table
    recommendations_data = [["Individual Tests", ""]]
    for test in data['Tests']:
        if 'recommendation' in test:
            recommendation = Paragraph(test['recommendation'], styles['Normal'])
            recommendations_data.append([test['testname'], recommendation])

    if len(recommendations_data) > 1:
        rec_table = Table(recommendations_data, colWidths=[105, 430])
        rec_table.setStyle(TableStyle([
            ('SPAN', (0, 0), (1, 0)),
            ('ALIGN', (0, 0), (1, 0), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkseagreen),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 1), (-1, 0), 'Helvetica'),


            ('FONTSIZE', (0, 1), (-1, -1), 8),
        ]))
        rec_table.wrapOn(c, width, height)

        # Draw the recommendations table
        rec_table.drawOn(c, 50,
                         table_start_y - rec_table._height)  # Use the table height to adjust the position dynamically

    c.save()
    print(f"PDF report created successfully: {pdf_file}")


def generate_pdf_for_client(db_file, client_id, date):
    client_data = load_data_from_db(db_file, client_id, date)
    if client_data:
        # Add static data for the example
        client_data['date'] = date
        client_data[
            'Referral_Statement'] = 'Refer to a Sports and Exercise Science Practitioner to improve your Fitness Quotient and for targeted interventions immediately.'

        create_pdf(client_data)

# Database file
db_file = "C:/Users/Admin/Downloads/Genpopulation (6).db"

# Generate PDF for a specific client ID and date
client_id = 'KANYGOHO_0005'
date = '2024-06-21'
generate_pdf_for_client(db_file, client_id, date)
