import streamlit as st
import pandas as pd
@st.cache(allow_output_mutation=True)
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'MobNo', 'BorNB', 'Age', 'Gender', 'TS1', 'TS2', 'TS3', 'TS4', 'TS5', 'BTS6', 'NBTS6'])
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def display_user_details(user_id, data):
    user_details = data[data['Name'] == user_id] if user_id in data['Name'].values else data[data['MobNo'] == user_id]
    user_details = user_details[['Name', 'MobNo', 'BorNB', "Age", "Gender"]]
    st.write(user_details)
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

if __name__ == "__main__":
    main()
