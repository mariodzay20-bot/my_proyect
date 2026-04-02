import pandas as pd
import plotly.express as px
import streamlit as st
st.title("Data Visualization with Streamlit")
st.write("This is a simple data visualization app using Streamlit.")
# Load data
data = pd.read_csv("notebook/vehicles_us.csv")
# Display data
st.write("Here is the data:")
st.dataframe(data)
# Create a plot
fig = px.scatter(data, x="Column1", y="Column2", title="Scatter Plot")
# Display the plot
st.plotly_chart(fig)
