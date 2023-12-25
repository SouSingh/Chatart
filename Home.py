import streamlit as st
from code import overall
from Pdf import main

# Sidebar navigation buttons
if st.sidebar.button("Chat_ai", key="home_button", help="Click to go home"):
    st.title("ChatART")
    st.write("Welcome to the World of ART")

if st.sidebar.button("Artist_Form", key="page1_button", help="Click to go to Artist_form"):
    st.title("Atist Corner")
    st.write("Welcome to Artist fill up center")
    overall()

if st.sidebar.button("Document Upload", key="page2_button", help="Click to go to Page 2"):
    st.title("Research paper Collector")
    st.write("Upload Your ART paper and our AI will help find your answer in smart manner.")
    main()
