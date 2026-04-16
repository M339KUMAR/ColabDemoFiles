
import streamlit as st
import pandas as pd

# df = pd.read_excel('/content/sample_data/HHS_Unaccompanied_Alien_Children_Program.xlsx')
# df = pd.read_excel('UM DA Mar_Jun/UMDAP1/HHS_Unaccompanied_Alien_Children_Program.xlsx')
df = pd.read_excel('HHS_Unaccompanied_Alien_Children_Program.xlsx', engine= 'openpyxl')
st.title("Hello from Colab via ngrok")
st.write("This works!")
st.dataframe(df)
st.write("Hello PRAVEENKUMAR MOPURU")
