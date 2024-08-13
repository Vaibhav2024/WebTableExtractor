import streamlit as st
import pandas as pd

st.title("Convert Web Page Data to .CSV file")
website_link = st.text_input("Paste Link Of Website...")
unique_char = st.text_input("If a Website Contains More than 1 Table Enter a Unique Column Name to Get Table of Your Like..(Optional)")
df = []
if website_link:
    try:
        df = pd.read_html(website_link, match=unique_char, header=0)
        country_code = df[0]
        st.write(country_code)
    except Exception as e:
        st.write(f"Error: {e}. Please make sure the URL is correct and the table exists.")


if st.button("Want to Download Specific Columns from above Data..."):
    input1 = st.text_input("Enter Column Name Separated with (,) Comma,  Ex: Serving, Cloth, Shoes")

    if df and input1:
        input_list1 = [item.strip() for item in input1.split(",")]
        try:
            df1 = country_code[input_list1]
            st.write(df1)
        except KeyError as e:
            st.write(f"Error: {e}. Please check that the column names are correct.")

