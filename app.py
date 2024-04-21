import streamlit as st
import pandas as pd


def ts1(TS1, Gender, Age):
    if TS1 == '' or pd.isna(TS1):
        return "Marks not entered"
    if Gender == "Female":
        if 20 <= Age <= 39:
            if TS1 >= 35:
                return "Above Average"
            elif 22 <= TS1 <= 34:
                return "Average"
            else:
                return "Below Average"
        elif 40 <= Age <= 59:
            if TS1 >= 36:
                return "Above Average"
            elif 24 <= TS1 <= 35:
                return "Average"
            else:
                return "Below Average"
        elif Age >= 60:
            if TS1 >= 37:
                return "Above Average"
            elif 25 <= TS1 <= 36:
                return "Average"
            else:
                return "Below Average"
    elif Gender == "Male":
        if 20 <= Age <= 39:
            if TS1 >= 25:
                return "Above Average"
            elif TS1 <= 8:
                return "Below Average"
            else:
                return "Average"
        elif 40 <= Age <= 59:
            if TS1 >= 27:
                return "Above Average"
            elif 12 <= TS1 <= 26:
                return "Average"
            else:
                return "Below Average"
        elif Age >= 60:
            if TS1 >= 29:
                return "Above Average"
            elif 14 <= TS1 <= 28:
                return "Average"
            else:
                return "Below Average"
    return "Invalid TS1"

def ts2(TS2, Gender, Age):
    if TS2 == '' or pd.isna(TS2):
        return "Marks not entered"
    if Gender == "Female":
        if 20 <= Age <= 29:
            if TS2 >= 30:
                return "Above Average"
            elif 18 <= TS2 <= 29:
                return "Average"
            else:
                return "Below Average"
        elif 30 <= Age <= 39:
            if TS2 >= 30:
                return "Above Average"
            elif 17 <= TS2 <= 29:
                return "Average"
            else:
                return "Below Average"
        elif 40 <= Age <= 49:
            if TS2 >= 27:
                return "Above Average"
            elif 15 <= TS2 <= 26:
                return "Average"
            else:
                return "Below Average"
        elif 50 <= Age <= 59:
            if TS2 >= 25:
                return "Above Average"
            elif 13 <= TS2 <= 24:
                return "Average"
            else:
                return "Below Average"
        elif Age >= 60:
            if TS2 >= 24:
                return "Above Average"
            elif 11 <= TS2 <= 23:
                return "Average"
            else:
                return "Below Average"
    elif Gender == "Male":
        if 20 <= Age <= 29:
            if TS2 >= 25:
                return "Above Average"
            elif TS2 <= 7:
                return "Below Average"
            else:
                return "Average"
        elif 30 <= Age <= 39:
            if TS2 >= 22:
                return "Above Average"
            elif 8 <= TS2 <= 21:
                return "Average"
            else:
                return "Below Average"
        elif 40 <= Age <= 49:
            if TS2 >= 18:
                return "Above Average"
            elif 5 <= TS2 <= 17:
                return "Average"
            else:
                return "Below Average"
        elif 50 <= Age <= 59:
            if TS2 >= 16:
                return "Above Average"
            elif 4 <= TS2 <= 15:
                return "Average"
            else:
                return "Below Average"
        elif Age >= 60:
            if TS2 >= 14:
                return "Above Average"
            elif TS2 <= 4:
                return "Below Average"
            else:
                return "Average"
    return "Invalid TS2"


def ts3(TS3, Gender, Age):
    if TS3 == '' or pd.isna(TS3):
        return "Marks not entered"
    if Gender == "Female":
        if 10 <= Age <= 11:
            if TS3 < 11.8:
                return "Below Average"
            elif 11.8 <= TS3 <= 21.6:
                return "Average"
            else:
                return "Above Average"
        elif 12 <= Age <= 13:
            if TS3 < 14.6:
                return "Below Average"
            elif 14.6 <= TS3 <= 24.4:
                return "Average"
            else:
                return "Above Average"
        elif 14 <= Age <= 15:
            if TS3 < 15.5:
                return "Below Average"
            elif 15.5 <= TS3 <= 27.3:
                return "Average"
            else:
                return "Above Average"
        elif 16 <= Age <= 17:
            if TS3 < 17.2:
                return "Below Average"
            elif 17.2 <= TS3 <= 29.0:
                return "Average"
            else:
                return "Above Average"
        elif 18 <= Age <= 19:
            if TS3 < 19.2:
                return "Below Average"
            elif 19.2 <= TS3 <= 31.0:
                return "Average"
            else:
                return "Above Average"
        elif 20 <= Age <= 24:
            if TS3 < 21.5:
                return "Below Average"
            elif 21.5 <= TS3 <= 35.3:
                return "Average"
            else:
                return "Above Average"
        elif 25 <= Age <= 29:
            if TS3 < 25.6:
                return "Below Average"
            elif 25.6 <= TS3 <= 41.4:
                return "Average"
            else:
                return "Above Average"
        elif 30 <= Age <= 34:
            if TS3 < 21.5:
                return "Below Average"
            elif 21.5 <= TS3 <= 35.3:
                return "Average"
            else:
                return "Above Average"
        elif 35 <= Age <= 39:
            if TS3 < 20.3:
                return "Below Average"
            elif 20.3 <= TS3 <= 34.1:
                return "Average"
            else:
                return "Above Average"
        elif 40 <= Age <= 44:
            if TS3 < 18.9:
                return "Below Average"
            elif 18.9 <= TS3 <= 32.7:
                return "Average"
            else:
                return "Above Average"
        elif 45 <= Age <= 49:
            if TS3 < 18.6:
                return "Below Average"
            elif 18.6 <= TS3 <= 32.4:
                return "Average"
            else:
                return "Above Average"
        elif 50 <= Age <= 54:
            if TS3 < 18.1:
                return "Below Average"
            elif 18.1 <= TS3 <= 31.9:
                return "Average"
            else:
                return "Above Average"
        elif 55 <= Age <= 59:
            if TS3 < 17.7:
                return "Below Average"
            elif 17.7 <= TS3 <= 31.5:
                return "Average"
            else:
                return "Above Average"
        elif 60 <= Age <= 64:
            if TS3 < 17.2:
                return "Below Average"
            elif 17.2 <= TS3 <= 31.0:
                return "Average"
            else:
                return "Above Average"
        elif 65 <= Age <= 69:
            if TS3 < 15.4:
                return "Below Average"
            elif 15.4 <= TS3 <= 27.2:
                return "Average"
            else:
                return "Above Average"
        elif Age >= 70:
            if TS3 < 14.7:
                return "Below Average"
            elif 14.7 <= TS3 <= 24.5:
                return "Average"
            else:
                return "Above Average"

    elif Gender == "Male":
        if 10 <= Age <= 11:
            if TS3 < 12.6:
                return "Below Average"
            elif 12.6 <= TS3 <= 22.4:
                return "Average"
            else:
                return "Above Average"
        elif 12 <= Age <= 13:
            if TS3 < 19.4:
                return "Below Average"
            elif 19.4 <= TS3 <= 31.2:
                return "Average"
            else:
                return "Above Average"
        elif 14 <= Age <= 15:
            if TS3 < 28.5:
                return "Below Average"
            elif 28.5 <= TS3 <= 44.3:
                return "Average"
            else:
                return "Above Average"
        elif 16 <= Age <= 17:
            if TS3 < 32.6:
                return "Below Average"
            elif 32.6 <= TS3 <= 52.4:
                return "Average"
            else:
                return "Above Average"
        elif 18 <= Age <= 19:
            if TS3 < 35.7:
                return "Below Average"
            elif 35.7 <= TS3 <= 55.5:
                return "Average"
            else:
                return "Above Average"
        elif 20 <= Age <= 24:
            if TS3 < 36.8:
                return "Below Average"
            elif 36.8 <= TS3 <= 56.6:
                return "Average"
            else:
                return "Above Average"
        elif 25 <= Age <= 29:
            if TS3 < 37.7:
                return "Below Average"
            elif 37.7 <= TS3 <= 57.5:
                return "Average"
            else:
                return "Above Average"
        elif 30 <= Age <= 34:
            if TS3 < 36.0:
                return "Below Average"
            elif 36.0 <= TS3 <= 55.8:
                return "Average"
            else:
                return "Above Average"
        elif 35 <= Age <= 39:
            if TS3 < 35.8:
                return "Below Average"
            elif 35.8 <= TS3 <= 55.6:
                return "Average"
            else:
                return "Above Average"
        elif 40 <= Age <= 44:
            if TS3 < 35.5:
                return "Below Average"
            elif 35.5 <= TS3 <= 55.3:
                return "Average"
            else:
                return "Above Average"
        elif 45 <= Age <= 49:
            if TS3 < 34.7:
                return "Below Average"
            elif 34.7 <= TS3 <= 54.5:
                return "Average"
            else:
                return "Above Average"
        elif 50 <= Age <= 54:
            if TS3 < 32.9:
                return "Below Average"
            elif 32.9 <= TS3 <= 50.7:
                return "Average"
            else:
                return "Above Average"
        elif 55 <= Age <= 59:
            if TS3 < 30.7:
                return "Below Average"
            elif 30.7 <= TS3 <= 48.5:
                return "Average"
            else:
                return "Above Average"
        elif Age >= 60:
            if TS3 < 30.2:
                return "Below Average"
            elif 30.2 <= TS3 <= 48.0:
                return "Average"
            else:
                return "Above Average"
    return "Invalid TS3"

#ts4
def ts4(TS4, Gender):
    if TS4 == '' or pd.isna(TS4):
        return "Marks not entered"
    if Gender == "Male":
        if TS4 >= 34:
            return "Above Average"
        elif 28 <= TS4 <= 33:
            return "Average"
        elif TS4 <= 27:
            return "Below Average"
    elif Gender == "Female":
        if TS4 >= 29:
            return "Above Average"
        elif 21 <= TS4 <= 28:
            return "Average"
        elif TS4 <= 20:
            return "Below Average"
    return "Invalid TS4"

def ts5(TS5, Gender, Age):
    if TS5 == '' or pd.isna(TS5):
        return "Marks not entered"
    if Gender == "Male":
        if 18 <= Age <= 25:
            if TS5 <= 79:
                return "Above Average"
            elif 80 <= TS5 <= 99:
                return "Average"
            else:
                return "Below Average"
        elif 26 <= Age <= 35:
            if TS5 <= 85:
                return "Above Average"
            elif 86 <= TS5 <= 111:
                return "Average"
            else:
                return "Below Average"
        elif 36 <= Age <= 45:
            if TS5 <= 88:
                return "Above Average"
            elif 89 <= TS5 <= 114:
                return "Average"
            else:
                return "Below Average"
        elif 46 <= Age <= 55:
            if TS5 <= 94:
                return "Above Average"
            elif 95 <= TS5 <= 120:
                return "Average"
            else:
                return "Below Average"
        elif 56 <= Age <= 65:
            if TS5 <= 97:
                return "Above Average"
            elif 98 <= TS5 <= 127:
                return "Average"
            else:
                return "Below Average"
        elif Age > 65:
            if TS5 <= 100:
                return "Above Average"
            elif 101 <= TS5 <= 125:
                return "Average"
            else:
                return "Below Average"
    elif Gender == "Female":
        if 18 <= Age <= 25:
            if TS5 <= 85:
                return "Above Average"
            elif 86 <= TS5 <= 103:
                return "Average"
            else:
                return "Below Average"
        elif 26 <= Age <= 35:
            if TS5 <= 92:
                return "Above Average"
            elif 93 <= TS5 <= 109:
                return "Average"
            else:
                return "Below Average"
        elif 36 <= Age <= 45:
            if TS5 <= 96:
                return "Above Average"
            elif 97 <= TS5 <= 114:
                return "Average"
            else:
                return "Below Average"
        elif 46 <= Age <= 55:
            if TS5 <= 101:
                return "Above Average"
            elif 102 <= TS5 <= 119:
                return "Average"
            else:
                return "Below Average"
        elif 56 <= Age <= 65:
            if TS5 <= 105:
                return "Above Average"
            elif 106 <= TS5 <= 128:
                return "Average"
            else:
                return "Below Average"
        elif Age > 65:
            if TS5 <= 101:
                return "Above Average"
            elif 102 <= TS5 <= 125:
                return "Average"
            else:
                return "Below Average"
    return "Invalid TS5"

def bts6(BTS6):
    if BTS6 == '' or pd.isna(BTS6):
        return "Marks not entered"
    if BTS6 <= 24:
        return "Below Average"
    elif 25 <= BTS6 <= 39:
        return "Average"
    elif 40 <= BTS6 <= 60:
        return "Above Average"
    else:
        return "Invalid BTS6"

def nbts6(NBTS6, Gender, Age):
    if NBTS6 == '' or pd.isna(NBTS6):
        return "Marks not entered"
    if Gender == "Male":
        if 18 <= Age <= 25:
            if NBTS6 >= 49:
                return "Above Average"
            elif 31 <= NBTS6 <= 48:
                return "Average"
            else:
                return "Below Average"
        elif 26 <= Age <= 35:
            if NBTS6 >= 45:
                return "Above Average"
            elif 29 <= NBTS6 <= 44:
                return "Average"
            else:
                return "Below Average"
        elif 36 <= Age <= 45:
            if NBTS6 >= 41:
                return "Above Average"
            elif 23 <= NBTS6 <= 40:
                return "Average"
            else:
                return "Below Average"
        elif 46 <= Age <= 55:
            if NBTS6 >= 35:
                return "Above Average"
            elif 18 <= NBTS6 <= 34:
                return "Average"
            else:
                return "Below Average"
        elif 56 <= Age <= 65:
            if NBTS6 >= 31:
                return "Above Average"
            elif 13 <= NBTS6 <= 30:
                return "Average"
            else:
                return "Below Average"
        elif Age > 65:
            if NBTS6 >= 28:
                return "Above Average"
            elif 11 <= NBTS6 <= 27:
                return "Average"
            else:
                return "Below Average"
    elif Gender == "Female":
        if 18 <= Age <= 25:
            if NBTS6 >= 43:
                return "Above Average"
            elif 25 <= NBTS6 <= 42:
                return "Average"
            else:
                return "Below Average"
        elif 26 <= Age <= 35:
            if NBTS6 >= 39:
                return "Above Average"
            elif 21 <= NBTS6 <= 38:
                return "Average"
            else:
                return "Below Average"
        elif 36 <= Age <= 45:
            if NBTS6 >= 33:
                return "Above Average"
            elif 15 <= NBTS6 <= 32:
                return "Average"
            else:
                return "Below Average"
        elif 46 <= Age <= 55:
            if NBTS6 >= 27:
                return "Above Average"
            elif 10 <= NBTS6 <= 26:
                return "Average"
            else:
                return "Below Average"
        elif 56 <= Age <= 65:
            if NBTS6 >= 24:
                return "Above Average"
            elif 7 <= NBTS6 <= 23:
                return "Average"
            else:
                return "Below Average"
        elif Age > 65:
            if NBTS6 >= 23:
                return "Above Average"
            elif 5 <= NBTS6 <= 22:
                return "Average"
            else:
                return "Below Average"
    return "Invalid NBTS6"
@st.cache(allow_output_mutation=True)
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'MobNo', 'BorNB', 'Age', 'Gender', 'TS1', 'TS2', 'TS3', 'TS4', 'TS5', 'BTS6', 'NBTS6'])
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)


# Function to display user details
def display_user_details(user_id, data):
    user_details = data[data['Name'] == user_id] if user_id in data['Name'].values else data[data['MobNo'] == user_id]
    user_details = user_details[['Name', 'MobNo', 'BorNB', "Age", "Gender"]]
    st.write(user_details)


# Function to update user marks
@st.cache(allow_output_mutation=True)
def update_user_marks(user_id, data, marks):
    index = data.index[data['Name'] == user_id].tolist()
    if not index:
        index = data.index[data['MobNo'] == user_id].tolist()
    for i in index:
        data.at[i, 'TS1'] = marks['TS1']
        data.at[i, 'TS2'] = marks['TS2']
        data.at[i, 'TS3'] = marks['TS3']
        data.at[i, 'TS4'] = marks['TS4']
        data.at[i, 'TS5'] = marks['TS5']
        if 'BTS6' in marks:
            data.at[i, 'BTS6'] = marks['BTS6']
        elif 'NBTS6' in marks:
            data.at[i, 'NBTS6'] = marks['NBTS6']

    # Apply score calculation functions
    data['ts1_C'] = data.apply(lambda row: ts1(row['TS1'], row['Gender'], row['Age']), axis=1)
    data['ts2_C'] = data.apply(lambda row: ts2(row['TS2'], row['Gender'], row['Age']), axis=1)
    data['ts3_C'] = data.apply(lambda row: ts3(row['TS3'], row['Gender'], row['Age']), axis=1)
    data['ts4_C'] = data.apply(lambda row: ts4(row['TS4'], row['Gender']), axis=1)
    data['ts5_C'] = data.apply(lambda row: ts5(row['TS5'], row['Gender'], row['Age']), axis=1)
    data['bts6_C'] = data.apply(lambda row: bts6(row['BTS6']) if 'BTS6' in row else None, axis=1)
    data['nbts6_C'] = data.apply(lambda row: nbts6(row['NBTS6'], row['Gender'], row['Age']) if 'NBTS6' in row else None, axis=1)

    return data

def calculate_counts(row):
    below_average_count = sum(x == "Below Average" for x in row[['ts1_C', 'ts2_C', 'ts3_C', 'ts4_C', 'ts5_C', 'bts6_C', 'nbts6_C']])
    average_count = sum(x == "Average" for x in row[['ts1_C', 'ts2_C', 'ts3_C', 'ts4_C', 'ts5_C', 'bts6_C', 'nbts6_C']])
    above_average_count = sum(x == "Above Average" for x in row[['ts1_C', 'ts2_C', 'ts3_C', 'ts4_C', 'ts5_C', 'bts6_C', 'nbts6_C']])
    return below_average_count, average_count, above_average_count

def main():
    st.title('Gen Population Testing Battery')

    file_path = 'C:/Users/Admin/Desktop/gen/SimData - SimData.csv'
    data = load_data(file_path)


    # Select search option
    select_option = st.sidebar.selectbox('Select search option:', ['Name', 'Phone Number'])

    if select_option == 'Name':
        names = data['Name'].unique()
        selected_name = st.sidebar.selectbox('Select name:', names)
        display_user_details(selected_name, data)
    else:
        phone_numbers = data['MobNo'].unique()
        selected_phone = st.sidebar.selectbox('Select phone number:', phone_numbers)
        display_user_details(selected_phone, data)

    st.header('Update Marks')
    marks = {}
    test_type = st.radio('Select test type:', ['Beginner', 'Non Beginner'])
    col1, col2 = st.columns(2)
    marks['TS1'] = col1.number_input('Enter TS1:', value=0)
    marks['TS2'] = col1.number_input('Enter TS2:', value=0)
    marks['TS3'] = col1.number_input('Enter TS3:', value=0)
    marks['TS4'] = col2.number_input('Enter TS4:', value=0)
    marks['TS5'] = col2.number_input('Enter TS5:', value=0)
    if test_type == 'Beginner':
        marks['BTS6'] = col2.number_input('Enter BTS6:', value=0)
    else:
        marks['NBTS6'] = col2.number_input('Enter NBTS6:', value=0)

    update_marks_button = st.button('Update Marks')
    if update_marks_button:
        if select_option == 'Name':
            updated_data = update_user_marks(selected_name, data, marks)
        else:
            updated_data = update_user_marks(selected_phone, data, marks)

        updated_data['BA'], updated_data['A'], updated_data['AA'] = zip(*updated_data.apply(calculate_counts, axis=1))
        save_data(updated_data, file_path)
        st.success("Marks saved successfully!")

        col1.empty()
        col2.empty()

        st.subheader('Calculated Results')

        # Split the display into two columns
        col1, col2 = st.columns(2)

        # Display results in the first column
        with col1:
            if select_option == 'Name':
                st.write("TS1:",
                         f"{updated_data.loc[updated_data['Name'] == selected_name, 'TS1'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'ts1_C'].iloc[0]}")
                st.write("TS2:",
                         f"{updated_data.loc[updated_data['Name'] == selected_name, 'TS2'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'ts2_C'].iloc[0]}")
                st.write("TS3:",
                         f"{updated_data.loc[updated_data['Name'] == selected_name, 'TS3'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'ts3_C'].iloc[0]}")
            else:
                st.write("TS1:",
                         f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'TS1'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'ts1_C'].iloc[0]}")
                st.write("TS2:",
                         f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'TS2'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'ts2_C'].iloc[0]}")
                st.write("TS3:",
                         f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'TS3'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'ts3_C'].iloc[0]}")

        # Display results in the second column
        with col2:
            if select_option == 'Name':
                st.write("TS4:",
                         f"{updated_data.loc[updated_data['Name'] == selected_name, 'TS4'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'ts4_C'].iloc[0]}")
                st.write("TS5:",
                         f"{updated_data.loc[updated_data['Name'] == selected_name, 'TS5'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'ts5_C'].iloc[0]}")
                if test_type == 'Beginner':
                    st.write("BTS6:",
                             f"{updated_data.loc[updated_data['Name'] == selected_name, 'BTS6'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'bts6_C'].iloc[0]}")
                else:
                    st.write("NBTS6:",
                             f"{updated_data.loc[updated_data['Name'] == selected_name, 'NBTS6'].iloc[0]} {updated_data.loc[updated_data['Name'] == selected_name, 'nbts6_C'].iloc[0]}")
            else:
                st.write("TS4:",
                         f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'TS4'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'ts4_C'].iloc[0]}")
                st.write("TS5:",
                         f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'TS5'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'ts5_C'].iloc[0]}")
                if test_type == 'Beginner':
                    st.write("BTS6:",
                             f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'BTS6'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'bts6_C'].iloc[0]}")
                else:
                    st.write("NBTS6:",
                             f"{updated_data.loc[updated_data['MobNo'] == selected_phone, 'NBTS6'].iloc[0]} {updated_data.loc[updated_data['MobNo'] == selected_phone, 'nbts6_C'].iloc[0]}")

if __name__ == "__main__":
    main()

