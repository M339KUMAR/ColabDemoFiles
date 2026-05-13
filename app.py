# Date                                             
# Children apprehended and placed in CBP custody       
# Children in CBP custody                              
# Children transferred out of CBP custody             
# Children in HHS Care                               
# Children discharged from HHS Care
 

import streamlit as st
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#df = pd.read_excel('/content/sample_data/HHS_Unaccompanied_Alien_Children_Program.xlsx')
df = pd.read_excel('HHS_Unaccompanied_Alien_Children_Program.xlsx', engine='openpyxl')

#st.title("Hello from Colab via ngrok")
#st.write("This works!")

#st.title("Unified Mentor")

st.markdown("<h1 style='text-align: center;'>UNIFIED MENTOR</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Data Analytics Intern</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Project-1</h2>", unsafe_allow_html=True)
st.write("***📌US-HHS Unaccompanied Children Program  Dashboard***")

st.dataframe(df)
#st.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#st.write("----------------------------")
#st.write("Hello PRAVEENKUMAR MOPURU")
#st.write("----------------------------")

#st.dataframe(df['Date'])

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Children in CBP custody'], label="sin(x)")
ax.set_title("Children in CBP Custody")
ax.set_xlabel("Date")
ax.set_ylabel("CBP Custidy")
ax.legend()


# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort chronologically
df = df.sort_values('Date')

# Create complete daily index
df = df.set_index('Date').asfreq('D')

# Missing values
df = df.fillna(0)

# Logical constraints
df['Anomaly_Flag'] = 0

df.loc[(df['Children transferred out of CBP custody'] > df['Children in CBP custody']), 'Anomaly_Flag'] = 1
df.loc[(df['Children discharged from HHS Care'] > df['Children in HHS Care']), 'Anomaly_Flag'] = 1

# Total system load
df['Total_Load'] = df['Children in CBP custody'] + df['Children in HHS Care']

# Net intake
df['Net_Intake'] = df['Children transferred out of CBP custody'] - df['Children discharged from HHS Care']

# Growth rate
#df['Growth_Rate'] = df['Total_Load'].pct_change() * 100
df['Growth_Rate'] = (
    df['Total_Load'].pct_change() * 100
).fillna(0)

# Backlog indicator
df['Backlog'] = (df['Net_Intake'] > 0).astype(int)

df['7_day_avg'] = df['Total_Load'].rolling(7).mean()
df['14_day_avg'] = df['Total_Load'].rolling(14).mean()

last_avg = df['Total_Load'].rolling(7).mean().iloc[-1]

days=30

future_dates = pd.date_range(start=df.index[-1], periods=days+1)[1:]

forecast_values = [last_avg] * days

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast_Load': forecast_values
})


st.title("📊 HHS Care System Dashboard")

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("🔑 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Load", int(df['Total_Load'].iloc[-1]))
col2.metric("Net Intake", int(df['Net_Intake'].iloc[-1]))
col3.metric("Growth Rate %", round(df['Growth_Rate'].iloc[0], 2), "%")
col4.metric("Backlog Active", int(df['Backlog'].sum()))

st.sidebar.header("🔧 Filters")

# Date range selector
min_date = df.index.min()
max_date = df.index.max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# Metric toggle
metric = st.sidebar.selectbox(
    "Select Metric",
    ["Total", "Inflow", "Outflow", "Backlog"]
)

# Time granularity
granularity = st.sidebar.selectbox(
    "Time Granularity",
    ["Daily", "Weekly", "Monthly"]
)

#df_filtered = df[
#    (df['Date'] >= pd.to_datetime(date_range[0])) &
#    (df['Date'] <= pd.to_datetime(date_range[1]))
#]

df_filtered = df[
    (df.index >= pd.to_datetime(date_range[0])) &
    (df.index <= pd.to_datetime(date_range[1]))
]

# Resampling based on granularity
if granularity == "Weekly":
    df_filtered = df_filtered.resample('W').sum().reset_index()
elif granularity == "Monthly":
    df_filtered = df_filtered.resample('M').sum().reset_index()


