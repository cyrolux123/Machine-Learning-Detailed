import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## Display a Simple Text
st.write("This is a simple text")

## Create a DataFrame
df = pd.DataFrame({ 
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the DataFrame
st.write("Here is the DataFrame")
st.write(df)

## Create a Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

## Display the Line Chart
st.write("Here is the Line Chart")
st.line_chart(chart_data) 