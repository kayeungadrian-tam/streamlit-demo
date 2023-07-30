import streamlit as st
import pandas as pd
from io import StringIO


# File Uploader
def file_upload(label):
    uploaded_file = st.file_uploader(label)

    if uploaded_file is not None:
        return uploaded_file
    else:
        st.write("No file uploaded")
        return None


# Run Button
def run_button(uploaded_file):
    button = st.button("Run")
    if button and uploaded_file is not None:
        print("Re-run")
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)


# Main
def main():
    uploaded_file = file_upload("Upload a CSV file")
    run_button(uploaded_file)


if __name__ == "__main__":
    main()
