import streamlit as st
from coded import overall
from Writer import art_writing_portfolio

# Sidebar navigation buttons
if st.sidebar.button("Chat_ai", key="home_button", help="Click to go home"):
    st.title("ChatART")
    st.write("Welcome to the World of ART")

if st.sidebar.button("Artist_Form", key="page1_button", help="Click to go to Artist_form"):
    st.title("Atist Corner")
    st.write("Welcome to Artist fill up center")
    overall()

if st.sidebar.button("Artist_Writer", key="page2_button", help="Click to go to Page 2"):
    st.title("Artist Writer Corner")
    st.write("Upload Your ART paper and our AI will help find your answer in smart manner.")
    art_writing_portfolio()
