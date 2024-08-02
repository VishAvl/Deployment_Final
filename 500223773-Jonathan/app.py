import streamlit as st
import pandas as pd

# Title of the app
st.title("Machine Learning Task App")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Manual data entry
manual_data = st.text_area("Or enter your data manually (comma-separated values, one row per line)")

# If file is uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data from uploaded file:")
    st.write(data)

# If manual data is entered
elif manual_data:
    data = pd.DataFrame([x.split(',') for x in manual_data.split('\n')])
    st.write("Data from manual entry:")
    st.write(data)

# Perform analysis (basic example: descriptive statistics)
if 'data' in locals():
    st.write("Analysis Results:")
    st.write(data.describe())
