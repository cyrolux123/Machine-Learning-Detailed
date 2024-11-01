import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

age = st.slider("Enter your age: ", 1, 100, 25)
st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "Ruby", "Go"]
choice = st.selectbox("Choose a programming language: ", options)
st.write(f"You chose {choice}")

if name:
    st.write(f"Hello {name}")

data = {
    "Name" : ["Tom", "Nick", "John", "Alice"],
    "Age" : [25, 30, 35, 40],
    "City" : ["New York", "London", "Paris", "Berlin"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file: ", type = "csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)