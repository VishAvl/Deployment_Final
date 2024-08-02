import streamlit as st
import pandas as pd

def main():
    st.title("Machine Learning Task Application")

    # Option to upload data
    data_file = st.file_uploader("Upload a CSV file", type=["csv"])

    # Option to enter data manually
    data_input = st.text_area("Or enter your data manually (comma-separated values):")

    # Load data
    if data_file is not None:
        df = pd.read_csv(data_file)
        st.write("Data from uploaded file:")
        st.write(df)
    elif data_input:
        data = [x.split(',') for x in data_input.split('\n')]
        df = pd.DataFrame(data[1:], columns=data[0])
        st.write("Data from manual input:")
        st.write(df)
    else:
        st.write("Please upload a file or enter data manually.")

    # Placeholder for machine learning analysis
    if st.button("Run Analysis"):
        if data_file or data_input:
            # Here you can add your machine learning code.
            # For demonstration, we will just display a message.
            st.write("Running analysis...")
            analysis_result = "Sample analysis result"  # Replace with actual result
            st.write("Analysis Results:")
            st.write(analysis_result)
        else:
            st.write("No data available for analysis.")

if __name__ == '__main__':
    main()