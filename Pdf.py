import streamlit as st
import os
import PyPDF2
from PyPDF2 import PdfReader

def save_to_folder(uploaded_file, folder_path):
    # Get the file name
    file_name = uploaded_file.name

    with open(os.path.join(folder_path, file_name), 'wb') as file:
        file.write(uploaded_file.read())

    st.success(f"PDF pages successfully saved")

def main():
    st.title("Research paper Upload")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        folder_path = "./data"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if st.button("Convert and Save"):
            save_to_folder(uploaded_file, folder_path)

