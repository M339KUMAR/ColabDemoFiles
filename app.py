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
from ydata_profiling import ProfileReport
#from data_profiling.profile_report import ProfileReport
import streamlit.components.v1 as components

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

#from ydata_profiling import ProfileReport
report = ProfileReport(df, explorative=True)
# Save report
#profile.to_file("report.html")
html = report.to_html()

# Read HTML file
#with open("report.html", "r", encoding="utf-8") as f:
#     html = f.read()

# Display in Streamlit
components.html(html, height=1000, scrolling=True)

#st.dataframe(df['Date'])
st.title("📊 HHS Care System Dashboard")

col1, col2 = st.columns([0.75, 5])

with col1:
    # Create a Matplotlib figure
    #st.pyplot(fig)
    if st.button("Plot-1"):
       fig, ax = plt.subplots()
       ax.plot(df['Date'], df['Children in CBP custody'], color='orange', linestyle='--', label="Children in CBP Custody")
       ax.set_title("Children in CBP Custody")
       ax.set_xlabel("Date")
       ax.set_ylabel("CBP Custidy")
       ax.tick_params(axis='x', rotation=45)
       ax.legend()
       st.pyplot(fig)

with col2:
    st.write("Click the PLOT Button to Display the Graph")

# Convert datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort from oldest to newest
df = df.sort_values(by='Date', ascending=True)

col1, col2 = st.columns([0.75, 5])

with col1:
 if st.button("Plot-2"):
   df['Cumulative_Load'] = df['Children in CBP custody'].cumsum()
   # -----------------------------
   # Plot
   # -----------------------------
   fig, ax = plt.subplots(figsize=(10, 5))
   ax.plot(
       df['Date'],
       df['Cumulative_Load'],
       color='cyan',
       linestyle='-.',
       label = "Cumsum of Children in CBP Custody"
   )
   ax.set_title("Cumulative Load Over Time")
   ax.set_xlabel("Date")
   ax.set_ylabel("Cumulative Load")
   ax.legend()
   # Rotate x-axis labels
   plt.xticks(rotation=45)
   st.pyplot(fig)

with col2:
    st.write("Click the PLOT Button to Display the CumSum of CBP Custody")

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

#df['Growth_Rate'] = df['Total_Load'][-1]

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

# Total Load
current_load = df['Total_Load'].iloc[-1]
previous_load = df['Total_Load'].iloc[-2]
load_delta = current_load - previous_load

# Net Intake
current_intake = df['Net_Intake'].iloc[-1]
previous_intake = df['Net_Intake'].iloc[-2]
intake_delta = (current_intake - previous_intake)

# Growth Rate
current_growth = df['Growth_Rate'].iloc[-1]
previous_growth = df['Growth_Rate'].iloc[-2]
growth_delta = (current_growth - previous_growth)

# Backlog
current_backlog = df['Backlog'].sum()
previous_backlog = df['Backlog'].iloc[:-1].sum()
backlog_delta = (current_backlog- previous_backlog)

# st.title("📊 HHS Care System Dashboard")

# -------------------------------
# KPI SECTION
# -------------------------------
#st.subheader("🔑 Key Metrics")
st.subheader("🔑 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

#col1.metric("Total Load", int(df['Total_Load'].iloc[-1]), "+50",  delta_color ="normal" )
#col2.metric("Net Intake", int(df['Net_Intake'].iloc[-1]), "-1", delta_color ="normal" )
#col3.metric("Growth Rate %", round(df['Growth_Rate'].iloc[0], 2), "0%")
#col4.metric("Backlog Active", int(df['Backlog'].sum()), "+5", delta_color ="normal" )

with col1:
    st.metric(
        "Total Load",
        int(current_load),
        delta=f"{load_delta:+,.0f}",
        delta_color="normal"
    )

with col2:
    st.metric(
        "Net Intake",
        int(current_intake),
        delta=f"{intake_delta:+,.0f}",
        delta_color="normal"
    )

with col3:
    st.metric(
        "Growth Rate %",
        round(current_growth, 2),
        delta=f"{growth_delta:+.2f}%"
    )

with col4:
    st.metric(
        "Backlog Active",
        int(current_backlog),
        delta=f"{backlog_delta:+,.0f}",
        delta_color="normal"
    )

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


