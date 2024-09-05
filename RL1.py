import sqlite3
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC
from business_rules.variables import BaseVariables, numeric_rule_variable
import plotly.graph_objects as go
import numpy as np
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.platypus.frames import Frame
from reportlab.platypus import Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor


def get_client_remark(client_id, date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Fetch the client's remark based on clientid and date
    remark_query = "SELECT remarks FROM test_details WHERE clientid = ? AND date = ?"
    cursor.execute(remark_query, (client_id, date))
    remarks = cursor.fetchone()

    conn.close()

    # Return the remark if it exists and is not just whitespace
    return remarks[0].strip() if remarks and remarks[0].strip() else None


def create_gauge_plot(status, output_file):

    # Set the value and result label based on the status
    if status.lower() == 'below average':
        value = 25
        result_label = "Below Average"
        result_color = "black"
    elif status.lower() == 'average':
        value = 50
        result_label = "Average"
        result_color = "black"
    elif status.lower() == 'above average':
        value = 75
        result_label = "Above Average"
        result_color = "black"
    else:
        value = 0
        result_label = "Unknown"
        result_color = "grey"

    # Define the ranges for different colors
    range_endpoints = [0, 40, 70, 100]
    range_colors = ["red", "yellow", "green"]

    # Create the figure
    fig = go.Figure()

    # Add colored background bars
    for i in range(len(range_endpoints) - 1):
        fig.add_shape(
            type="rect",
            x0=range_endpoints[i],
            x1=range_endpoints[i + 1],
            y0=0,
            y1=1,
            fillcolor=range_colors[i],
            line=dict(width=0)
        )

        # Add constant text inside each color segment with bold formatting
        color_labels = ["<b>Below Average</b>", "<b>Average</b>", "<b>Above Average</b>"]
        fig.add_annotation(
            x=(range_endpoints[i] + range_endpoints[i + 1]) / 2,  # Center of the segment
            y=0.5,
            text=color_labels[i],
            showarrow=False,
            font=dict(size=50, color="black"),
            xref="x",
            yref="y",
            align="center"
        )

    # Add a V-shaped downward arrow
    arrow_length = 0.1
    arrow_width = 10
    fig.add_shape(
        type="path",
        path=f"M {value} 1.2 L {value - arrow_width / 2} {1.2 + arrow_length} L {value + arrow_width / 2} {1.2 + arrow_length} Z",
        fillcolor="black",
        line=dict(color="black")
    )

    # Add result text below the plot
    fig.add_annotation(
        x=0.5,
        y=-0.05,  # Position below the plot
        text=f"<b>{result_label}</b>",
        showarrow=False,
        font=dict(size=45, color=result_color),
        xref="paper",
        yref="paper",
        align="center"
    )

    # Update layout for the linear gauge
    fig.update_layout(
        height=500,
        width=1500,
        xaxis=dict(
            range=[0, 100],
            showticklabels=False
        ),
        yaxis=dict(
            range=[-0.5, 1.5],  # Extend y-axis to accommodate the arrow above the plot
            showticklabels=False
        ),
        plot_bgcolor="#ffffff",
        margin=dict(t=60, b=60, l=40, r=40)  # Increase top margin to fit the arrow above the plot
    )

    # Save the plot as an image
    fig.write_image(output_file)

def get_client_remark(client_id, date):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Fetch the client's remark based on clientid and date
    remark_query = "SELECT remarks FROM test_details WHERE clientid = ? AND date = ?"
    cursor.execute(remark_query, (client_id, date))
    remarks = cursor.fetchone()

    conn.close()

    # Return the remark if it exists and is not just whitespace
    return remarks[0].strip() if remarks and remarks[0].strip() else None

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
    def __init__(self, AA, A, BA, num_tests):
        self.AA = AA
        self.A = A
        self.BA = BA
        self.num_tests = num_tests

    def fq_string(self):
        if self.num_tests == 6:
            if self.AA == 6 or self.AA == 5:
                return 'VERY GOOD'
            elif self.AA == 4 or (self.AA == 3 and self.A > 0):
                return 'GOOD'
            elif (self.AA == 3 and self.A == 0) or (self.AA == 2) or (self.AA == 1 and self.BA == 0):
                return 'MODERATE'
            elif (self.AA == 1 and self.BA > 0) or (self.AA == 0 and self.A > 1):
                return 'POOR'
            elif self.AA == 0 and self.A <= 1:
                return 'VERY POOR'
            else:
                return 'UNKNOWN'
        elif self.num_tests == 7:
            if self.AA == 7 and self.A == 0 and self.BA == 0:
                return 'VERY GOOD'
            elif self.AA == 6 and self.A == 1 and self.BA == 0:
                return 'VERY GOOD'
            elif self.AA == 6 and self.A == 0 and self.BA == 1:
                return 'VERY GOOD'
            elif self.AA == 5 and self.A == 2 and self.BA == 0:
                return 'GOOD'
            elif self.AA == 5 and self.A == 1 and self.BA == 1:
                return 'GOOD'
            elif self.AA == 5 and self.A == 0 and self.BA == 2:
                return 'GOOD'
            elif self.AA == 4 and self.A == 3 and self.BA == 0:
                return 'GOOD'
            elif self.AA == 4 and self.A == 2 and self.BA == 1:
                return 'GOOD'
            elif self.AA == 4 and self.A == 1 and self.BA == 2:
                return 'GOOD'
            elif self.AA == 4 and self.A == 0 and self.BA == 3:
                return 'GOOD'
            elif self.AA == 3 and self.A == 4 and self.BA == 0:
                return 'GOOD'
            elif self.AA == 0 and self.A == 7 and self.BA == 0:
                return 'MODERATE'
            elif self.AA == 3 and self.A == 1 and self.BA == 3:
                return 'MODERATE'
            elif self.AA == 3 and self.A == 3 and self.BA == 1:
                return 'MODERATE'
            elif self.AA == 3 and self.A == 2 and self.BA == 2:
                return 'MODERATE'
            elif self.AA == 2 and self.A == 4 and self.BA == 1:
                return 'MODERATE'
            elif self.AA == 2 and self.A == 3 and self.BA == 2:
                return 'MODERATE'
            elif self.AA == 2 and self.A == 5 and self.BA == 0:
                return 'MODERATE'
            elif self.AA == 1 and self.A == 6 and self.BA == 0:
                return 'MODERATE'
            elif self.AA == 0 and self.A == 2 and self.BA == 5:
                return 'POOR'
            elif self.AA == 2 and self.A == 0 and self.BA == 5:
                return 'POOR'
            elif self.AA == 1 and self.A == 1 and self.BA == 5:
                return 'POOR'
            elif self.AA == 3 and self.A == 0 and self.BA == 4:
                return 'POOR'
            elif self.AA == 2 and self.A == 1 and self.BA == 4:
                return 'POOR'
            elif self.AA == 1 and self.A == 2 and self.BA == 4:
                return 'POOR'
            elif self.AA == 0 and self.A == 3 and self.BA == 4:
                return 'POOR'
            elif self.AA == 1 and self.A == 3 and self.BA == 3:
                return 'POOR'
            elif self.AA == 0 and self.A == 4 and self.BA == 3:
                return 'POOR'
            elif self.AA == 2 and self.A == 2 and self.BA == 3:
                return 'POOR'
            elif self.AA == 0 and self.A == 5 and self.BA == 2:
                return 'POOR'
            elif self.AA == 1 and self.A == 4 and self.BA == 2:
                return 'POOR'
            elif self.AA == 0 and self.A == 6 and self.BA == 1:
                return 'POOR'
            elif self.AA == 1 and self.A == 5 and self.BA == 1:
                return 'POOR'
            elif self.AA == 0 and self.A == 0 and self.BA == 7:
                return 'VERY POOR'
            elif self.AA == 0 and self.A == 1 and self.BA == 6:
                return 'VERY POOR'
            elif self.AA == 1 and self.A == 0 and self.BA == 6:
                return 'VERY POOR'
        return 'Unknown'


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

def calculate_fq(AA, A, BA, num_tests):
    fq_calculator = FQCalculator(AA, A, BA, num_tests)
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

    # Fetch organization data for the referral statement
    org_query = "SELECT company_name, city FROM organizations"
    cursor.execute(org_query)
    org_data = cursor.fetchone()

    if org_data:
        client_data['company_name'], client_data['city'] = org_data
    else:
        client_data['company_name'], client_data['city'] = 'Your Company Name', 'Your City'

    # Fetch test data with parametername for the current client
    test_query = """
    SELECT testname, parametername, status
    FROM test_details 
    WHERE clientid = ? AND date = ?
    """
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

    # Count the statuses and add recommendations
    status_counts = {'above average': 0, 'average': 0, 'below average': 0}
    for test in test_data:
        status = test['status'].lower()
        if status in status_counts:
            status_counts[status] += 1
        test['recommendation'] = recommendations_dict.get((test['testname'], status), '')

    # Calculate FQ and FQ_Numeric
    num_tests = len(test_data)
    client_data['AA'] = status_counts['above average']
    client_data['A'] = status_counts['average']
    client_data['BA'] = status_counts['below average']
    client_data['FQ'] = calculate_fq(client_data['AA'], client_data['A'], client_data['BA'], num_tests)
    client_data['FQ_Numeric'] = check_fq_grade(client_data['FQ'])

    conn.close()
    return client_data


def create_gauge(fq_numeric, output_path):
    plot_bgcolor = "#ffffff"
    quadrant_colors = ["#ffffff", "#2bad4e", "#85e043", "#eff229", "#f2a529", "#f25829"]
    quadrant_text = ["", "<b>Very Good</b>", "<b>Good</b>", "<b>Moderate</b>", "<b>Poor</b>", "<b>Very Poor</b>"]
    n_quadrants = len(quadrant_colors) - 1

    min_value = 0
    max_value = 5
    hand_length = np.sqrt(2) / 4

    # Adjust hand_angle to point to the middle of each quadrant
    hand_angle = np.pi * (1 - (max(min_value, min(max_value, fq_numeric - 0.5)) - min_value) / (max_value - min_value))

    # Determine the corresponding label and color based on fq_numeric
    if fq_numeric <= 1:
        label = "Very Poor"
        color = quadrant_colors[5]
    elif fq_numeric <= 2:
        label = "Poor"
        color = quadrant_colors[4]
    elif fq_numeric <= 3:
        label = "Moderate"
        color = quadrant_colors[3]
    elif fq_numeric <= 4:
        label = "Good"
        color = quadrant_colors[2]
    else:
        label = "Very Good"
        color = quadrant_colors[1]

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
                textfont=dict(size=40)  # Increase the font size of the quadrant text
            ),
        ],
        layout=go.Layout(
            showlegend=False,
            margin=dict(b=0, t=10, l=10, r=10),
            width=1000,  # Increased width
            height=1000,  # Increased height
            paper_bgcolor=plot_bgcolor,
            annotations=[
                go.layout.Annotation(
                    text=f"<b>{label}</b>",
                    x=0.5, xanchor="center", xref="paper",
                    y=0.4, yanchor="bottom", yref="paper",  # Adjusted y position for better alignment
                    showarrow=False,
                    font=dict(size=80, color=color)  # Use the corresponding color
                )
            ],
            shapes=[
                go.layout.Shape(
                    type="line",
                    x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                    y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                    line=dict(color="#333", width=7)  # Increased line width for better visibility
                )
            ]
        )
    )
    fig.write_image(output_path)

def draw_footer(c, logo1_path, logo2_path):
    header_height = 50  # Height of the footer section
    logo_width = 60     # Width of the logos
    logo_height = 45     # Height of the logos

    # Set the fill color to black for the footer background
    c.setFillColor(colors.black)
    # Draw the footer rectangle at the bottom of the page
    c.rect(0, 0, c._pagesize[0], header_height, fill=1)

    # Draw the first logo (on the left side)
    c.drawImage(logo1_path, 20, 5, width=logo_width, height=logo_height)

    # Draw the second logo (on the right side)
    c.drawImage(logo2_path, c._pagesize[0] - logo_width - 20, 5, width=logo_width, height=logo_height)
def create_pdf(data):
    pdf_file = f"Assessment_Report_{data['clientid']}_{data['date']}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    logo1_path = "C:/Users/Admin/Downloads/Logo.jpg"
    logo2_path = "C:/Users/Admin/Downloads/Logo.jpg"
    background_image_path = "C:/Users/Admin/Downloads/background_image.jpeg"

    # Image paths for the first and second pages
    image1_path = "C:/Users/Admin/Downloads/image1.png"
    image2_path = "C:/Users/Admin/Downloads/image2.png"
    image3_path = "C:/Users/Admin/Downloads/image3.png"
    image4_path = "C:/Users/Admin/Downloads/image4.png"
    image5_path = "C:/Users/Admin/Downloads/image5.png"

    # First page with background image
    background_image = ImageReader(background_image_path)
    c.drawImage(background_image, 0, 0, width=width, height=height)


    image_width1, image_height1 = 80, 70  # Adjust as needed
    image_width2, image_height2 = 150, 50
    image_width3, image_height3 = 200, 230  # Adjust as needed

    c.drawImage(image1_path, 480, height - 95, width=image_width1, height=image_height1)
    c.drawImage(image2_path, 390, height - 150, width=image_width2, height=image_height2)
    c.drawImage(image3_path, 405, height - 440, width=image_width3, height=image_height3)

    title = height - 200
    # Content: "Personal Fitness Report"
    title_text = "Personal Fitness Report"
    c.setFont("Helvetica", 24)
    c.setFillColorRGB(1, 1, 1)  # Set text color to white

    c.drawString(160, title, title_text)


    # Sky blue line below the title
    line_y = height - 210  # Adjust position for the line
    c.setStrokeColorRGB(0.529, 0.808, 0.922)  # Sky blue color (RGB: 135, 206, 235)
    c.setLineWidth(2)
    c.line(width * 0.2, line_y, width * 0.8, line_y)  # Draw the line

    # Content: "A Comprehensive Physical Fitness Analysis"
    content_text = "A Comprehensive Physical Fitness Analysis"
    c.setFont("Helvetica", 16)
    c.setFillColorRGB(1, 1, 1)  # Set text color to white
    content_width = c.stringWidth(content_text, "Helvetica", 16)
    c.drawString(160, line_y - 20, content_text)

    # Additional Information
    c.setFont("Helvetica", 15)
    c.drawString(200, line_y - 40, "(with your Fitness Quotient)")

    c.setFillColor(colors.black)
    # Address of client
    c.drawString(50, line_y - 350, "Assessed For: ")
    address_text = f"{data['name']}, {data['dob']}, {data['gender']}"
    c.drawString(50, line_y - 365, address_text)

    # Assessed on
    assessed_on_text = f"Assessed On: {data['date']}"
    c.drawString(50, line_y - 380, assessed_on_text)

    # Assessed by
    assessed_by_text = f"Assessed By: {data.get('company_name', 'Company Name not available')}"
    c.drawString(50, line_y - 395, assessed_by_text)

    # Reset stroke color and line width before drawing footer
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)

    # Draw the footer
    draw_footer(c, logo1_path, logo2_path)

    # Finalize the first page
    c.showPage()

    # Second page with colored background
    c.setFillColor(HexColor("#113154"))  # Set the background color to #113154
    c.rect(0, 0, width, height, stroke=0, fill=1)  # Draw the background rectangle

    # Add 2 images to the second page
    image_width, image_height = 300, 130  # Adjust as needed
    image_width2, image_height2 = 380, 350
    c.drawImage(image4_path, 150, height - 150, width=image_width, height=image_height)
    c.drawImage(image5_path, 150, height - 490, width=image_width2, height=image_height2)

    # Text content
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 12)
    details_y = height - 550  # Start below the header
    c.drawString(250, details_y, "Fitness Quotient (FQ)")
    image_width1, image_height1 = 20, 30
    image_width2, image_height2 = 18, 25# Adjust as needed
    c.drawImage(image1_path, 380, details_y - 5, width=image_width1, height=image_height1)
    # Sky blue line below the title
    line_y = height - 560  # Adjust position for the line
    c.setStrokeColorRGB(1,1,1)  # Sky blue color (RGB: 135, 206, 235)
    c.setLineWidth(2)
    c.line(width * 0.4, line_y, width * 0.6, line_y)  # Draw the line
    c.drawImage(image1_path, 90, details_y - 25, width=image_width2, height=image_height2)
    c.drawString(115, details_y - 25, "To evaluate overall physical health like cardiovascular endurance,strength,flexibility, and")
    c.drawString(115, details_y - 40, "body composition and how these factors affect Functional movement and Daily Activities.")
    c.drawImage(image1_path, 90, details_y - 80, width=image_width2, height=image_height2)
    c.drawString(115, details_y - 80, "The FQ provides insights into how physical fitness influences overall Quality of Life.")

    # Reset stroke color and line width before drawing footer
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    # Draw the footer on the second page
    draw_footer(c, logo1_path, logo2_path)

    # Finalize the second page
    c.showPage()
    # Personal details
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    details_y = height - 50  # Start below the header
    c.drawString(50, details_y, f"Name: {data['name']}")
    c.drawString(50, details_y - 20, f"Gender: {data['gender']}")
    c.drawString(350, details_y, f"Date of Birth: {data['dob']}")
    c.drawString(350, details_y - 20, f"Date: {data['date']}")


    # Define a mapping of parameter names to image files
    param_image_mapping = {
        "Aerobic Fitness": "C:/Users/Admin/Downloads/parameter_image_1.jpeg",
        "Flexibility": "C:/Users/Admin/Downloads/parameter_image_2.jpeg",
        "Muscular Strength UB": "C:/Users/Admin/Downloads/parameter_image_3.jpeg",
        "Muscular Strength LB": "C:/Users/Admin/Downloads/parameter_image_4.jpeg",
        "Muscular Endurance": "C:/Users/Admin/Downloads/parameter_image_5.jpeg",
        "Balance": "C:/Users/Admin/Downloads/parameter_image_6.jpeg",
        "Body Composition": "C:/Users/Admin/Downloads/parameter_image_7.jpeg"
    }


    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    c.drawString(50, details_y-40, f"Height: {data['height']}")
    c.drawString(350, details_y-40, f"Weight: {data['height']}")
    # Subtitle for Assessment Results
    c.setFillColor(colors.darkorange)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(280, details_y - 50, "Results")

    # Subtitle for Recommendations
    rec1_y = details_y - 50  # Adjust starting Y position for recommendations section

    # Fixed space between the title and the table
    space_between_title_and_table = 10  # Adjust this value as needed

    # Calculate the starting position for the recommendations table
    table_start_y = rec1_y - space_between_title_and_table  # Ensure it starts just below the title
    test_data = [["Parameter", "Test Name", "Level"]]
    styles = getSampleStyleSheet()

    for i, test in enumerate(data['Tests']):
        # Generate the gauge plot for each status
        gauge_image_file = f"{test['status'].replace(' ', '_').lower()}_gauge.png"
        create_gauge_plot(test['status'], gauge_image_file)

        # Fetch the corresponding image based on the parameter name
        param_name = test['parametername']
        param_image_file = param_image_mapping.get(param_name)
        param_image = Image(param_image_file, width=50, height=50)

        # Combine the parameter name and image
        param_name_paragraph = Paragraph(param_name, styles['Normal'])
        param_combined = [param_image, param_name_paragraph]

        # Include the gauge image in the table row
        gauge_image = Image(gauge_image_file, width=150, height=50)
        test_data.append([param_combined, test['testname'], gauge_image])

    # Define alternating row colors
    colors_list = [
        colors.antiquewhite,
        colors.gainsboro,
        colors.lemonchiffon,
        colors.aliceblue,
        colors.silver,
        colors.peachpuff,
        colors.gold
    ]

    # Create table and set style
    table = Table(test_data, colWidths=[180, 150, 200])
    num_rows = len(test_data)
    row_styles = []
    for i in range(1, num_rows):  # Skip header row
        color = colors_list[(i - 1) % len(colors_list)]
        row_styles.append(('BACKGROUND', (0, i), (-1, i), color))

    table.setStyle(TableStyle([
                                  ('BACKGROUND', (0, 0), (-1, 0), colors.black),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                  ('GRID', (0, 0), (-1, -1), 1, colors.white),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTSIZE', (0, 0), (-1, 0), 10),
                                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                  ('TOPPADDING', (0, 0), (-1, 0), 10),
                                  ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                                  ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                  ('FONTSIZE', (0, 1), (-1, -1), 10),
                              ] + row_styles))  # Apply alternating row colors
    table.wrapOn(c, width, height)

    # Draw the recommendations table
    table.drawOn(c, 50,
                     table_start_y - table._height)

    # Footer and other content...
    draw_footer(c, logo1_path, logo2_path)
    c.showPage()

    results_y = details_y - 500

    # Personal details
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    details_y = height - 50  # Start below the header
    c.drawString(50, details_y, f"Name: {data['name']}")
    c.drawString(50, details_y - 20, f"Gender: {data['gender']}")
    c.drawString(350, details_y, f"Date of Birth: {data['dob']}")
    c.drawString(350, details_y - 20, f"Date: {data['date']}")


    # Subtitle for Fitness Quotient
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(280, details_y - 40, "Summmary")
    # Subtitle for Fitness Quotient
    c.setFillColor(colors.darkorange)
    c.setFont("Helvetica", 10)
    c.drawString(50, details_y - 45, "Fitness Quotient")


    fq_y = details_y - 170

    # Gauge plot
    gauge_image_path = "gauge_plot.png"
    create_gauge(data['FQ_Numeric'], gauge_image_path)
    c.drawImage(gauge_image_path, 50, fq_y - 80, width=200, height=200)

    # Recommendation text
    recommendation_text = get_recommendation(data['FQ'])
    style = ParagraphStyle(
        name='Normal',
        fontSize=10,
        leading=20,
        spaceAfter=10,
        alignment=TA_CENTER  # Center align the text
    )
    recommendation_paragraph = Paragraph(recommendation_text, style)
    frame = Frame(280, fq_y - 125, 250, 250, showBoundary=0)
    frame.addFromList([recommendation_paragraph], c)



    # Subtitle for Recommendations
    rec1_y = fq_y - 5  # Adjust starting Y position for recommendations section



    # Recommendations Table
    recommendations_data = [["Recommendations", ""]]
    for test in data['Tests']:
        if 'recommendation' in test:
            # Create a Paragraph for both the parameter name and the recommendation
            parameter_paragraph = Paragraph(test['parametername'], styles['Normal'])
            recommendation = Paragraph(test['recommendation'], styles['Normal'])
            recommendations_data.append([parameter_paragraph, recommendation])


    if len(recommendations_data) > 1:
        rec_table = Table(recommendations_data, colWidths=[68, 460])
        rec_table.setStyle(TableStyle([
            ('SPAN', (0, 0), (1, 0)),
            ('ALIGN', (0, 0), (1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically center text
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('TOPPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # Center horizontally
            ('FONTNAME', (0, 1), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ]))
        rec_table.wrapOn(c, width, height)

        # Draw the recommendations table
        rec_table.drawOn(c, 50,
                         rec1_y - rec_table._height)  # Use the table height to adjust the position dynamically

        # Remarks Section
        client_remark = get_client_remark(data['clientid'], data['date'])  # Fetch remark using clientid and date

        if client_remark:
            remarks_y = table_start_y - rec_table._height - 130  # Position below the recommendations table
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(colors.darkorange)
            c.drawString(50, remarks_y, "Remarks")

            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)

            remarks_text = Paragraph(client_remark, styles['Normal'])
            remarks_text.wrapOn(c, 500, 100)
            remarks_text.drawOn(c, 50, remarks_y - 15)

    c.drawString(320, table_start_y - rec_table._height - 142, "Next Assessment on - 03-10-2024 ")
    # Referral Statement
    ref_y = table_start_y - rec_table._height - 140
    c.setFont("Helvetica-Bold", 10)
    ref_text = Paragraph(data['Referral_Statement'], styles['Normal'])
    ref_text.wrap(500, 500)
    ref_text.drawOn(c, 50, ref_y - 30)
    draw_footer(c, logo1_path, logo2_path)
    c.save()
    print(f"PDF report created successfully: {pdf_file}")


def generate_pdf_for_client(db_file, client_id, date):
    client_data = load_data_from_db(db_file, client_id, date)
    if client_data:
        # Add static data for the example
        client_data['date'] = date
        company_name = client_data.get('company_name', 'Your Company Name')
        city = client_data.get('city', 'Your City')

        client_data[
            'Referral_Statement'] = f'Refer to {company_name} in {city} to improve your Fitness Quotient and for targeted interventions immediately.'

        create_pdf(client_data)


# Database file
db_file = "C:/Users/Admin/Downloads/Genpopulation (10).db"

# Generate PDF for a specific client ID and date
client_id = 'CHENGANS_0004'
date = '12-08-2024'
generate_pdf_for_client(db_file, client_id, date)
