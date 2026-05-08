
import streamlit as st
import pandas as pd
import openpyxl

#df = pd.read_excel('/content/sample_data/HHS_Unaccompanied_Alien_Children_Program.xlsx')
df = pd.read_excel('HHS_Unaccompanied_Alien_Children_Program.xlsx', engine='openpyxl')
st.title("Hello from Colab via ngrok")
st.write("This works!")
st.dataframe(df)
st.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
st.write("----------------------------")
st.write("Hello PRAVEENKUMAR MOPURU")
st.write("----------------------------")
st.dataframe(df['Date'])


st.sidebar.header("🔧 Filters")

# Date range selector
min_date = df['Date'].min()
max_date = df['Date'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)
