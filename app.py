import streamlit as st
import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("File not found!")
        st.stop()  # Stop execution if file not found
    return df

def main():
    st.title('Select Name from CSV')

    file_path = 'C:/Users/Admin/Desktop/gen/SimData - SimData.csv'  # Update with your CSV file path
    data = load_data(file_path)

    selected_name = st.selectbox('Select Name:', data['Name'].unique())

    st.write("You selected:", selected_name)

if __name__ == "__main__":
    main()
