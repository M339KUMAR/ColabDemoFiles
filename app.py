# Date                                             
# Children apprehended and placed in CBP custody       
# Children in CBP custody                              
# Children transferred out of CBP custody             
# Children in HHS Care                               
# Children discharged from HHS Care


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

df.loc[(df['Transfers'] > df['CBP_Custody']), 'Anomaly_Flag'] = 1
df.loc[(df['Discharges'] > df['HHS_Care']), 'Anomaly_Flag'] = 1

# Total system load
df['Total_Load'] = df['CBP_Custody'] + df['HHS_Care']

# Net intake
df['Net_Intake'] = df['Transfers'] - df['Discharges']

# Growth rate
df['Growth_Rate'] = df['Total_Load'].pct_change() * 100

# Backlog indicator
df['Backlog'] = (df['Net_Intake'] > 0).astype(int)

df['7_day_avg'] = df['Total_Load'].rolling(7).mean()
df['14_day_avg'] = df['Total_Load'].rolling(14).mean()

last_avg = df['Total_Load'].rolling(7).mean().iloc[-1]

future_dates = pd.date_range(start=df.index[-1], periods=days+1)[1:]

forecast_values = [last_avg] * days

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast_Load': forecast_values
})

st.set_page_config(layout="wide")

st.title("📊 HHS Care System Dashboard")


st.sidebar.header("🔧 Filters")

# Date range selector
min_date = df['Date'].min()
max_date = df['Date'].max()

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

df_filtered = df[
    (df['Date'] >= pd.to_datetime(date_range[0])) &
    (df['Date'] <= pd.to_datetime(date_range[1]))
]

# Resampling based on granularity
if granularity == "Weekly":
    df_filtered = df_filtered.set_index('Date').resample('W').sum().reset_index()
elif granularity == "Monthly":
    df_filtered = df_filtered.set_index('Date').resample('M').sum().reset_index()


data = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Chennai", "Delhi", "Mumbai"],
    "Sales": [100, 200, 150, 300, 250]
})

st.sidebar.title("Filters")

city = st.sidebar.selectbox("Select City", data["City"].unique())

filtered_data = data[data["City"] == city]

st.write(filtered_data)

col1, col2 = st.columns(2)

with col1:
    st.metric("Revenue", 50000)

with col2:
    st.metric("Profit", 12000)
