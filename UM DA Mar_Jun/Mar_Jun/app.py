
import streamlit as st
import pandas as pd

df = pd.read_excel('/content/sample_data/HHS_Unaccompanied_Alien_Children_Program.xlsx')
st.title("Hello from Colab via ngrok")
st.write("This works!")
st.dataframe(df)
st.write("Hello PRAVEENKUMAR MOPURU")
