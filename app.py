
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

# -----------------------------
# KPI CALCULATIONS
# -----------------------------
total_load = df_filtered['Total'].sum()
total_inflow = df_filtered['Inflow'].sum()
total_outflow = df_filtered['Outflow'].sum()
backlog = df_filtered['Backlog'].iloc[-1]

balance = total_inflow - total_outflow


# -----------------------------
# KPI SUMMARY CARDS
# -----------------------------
st.subheader("📌 KPI Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Load", f"{total_load:,}")
col2.metric("Inflow", f"{total_inflow:,}")
col3.metric("Outflow", f"{total_outflow:,}")
col4.metric("Backlog", f"{backlog:,}", delta=f"{balance:,}")


# -----------------------------
# SYSTEM LOAD OVERVIEW
# -----------------------------
st.subheader("📈 System Load Overview")

fig1, ax1 = plt.subplots()
ax1.plot(df_filtered['Date'], df_filtered['Total'])
ax1.set_title("Total System Load Over Time")
st.pyplot(fig1)

# -----------------------------
# CBP vs HHS COMPARISON
# -----------------------------
st.subheader("⚖️ CBP vs HHS Load Comparison")

fig2, ax2 = plt.subplots()
ax2.plot(df_filtered['Date'], df_filtered['CBP'], label='CBP')
ax2.plot(df_filtered['Date'], df_filtered['HHS'], label='HHS')
ax2.legend()
ax2.set_title("CBP vs HHS Load")
st.pyplot(fig2)

# -----------------------------
# NET INTAKE & BACKLOG
# -----------------------------
st.subheader("📊 Net Intake & Backlog Trends")

df_filtered['Net Intake'] = df_filtered['Inflow'] - df_filtered['Outflow']

fig3, ax3 = plt.subplots()
ax3.plot(df_filtered['Date'], df_filtered['Net Intake'], label="Net Intake")
ax3.plot(df_filtered['Date'], df_filtered['Backlog'], label="Backlog")
ax3.legend()
ax3.set_title("Net Intake & Backlog")
st.pyplot(fig3)

# -----------------------------
# CAPACITY STRESS ANALYSIS
# -----------------------------
st.subheader("🚨 Capacity Stress & Relief")

threshold = df_filtered['Total'].mean()

df_filtered['Stress'] = df_filtered['Total'] > threshold

fig4, ax4 = plt.subplots()
ax4.plot(df_filtered['Date'], df_filtered['Total'])
ax4.axhline(threshold)
ax4.set_title("Stress Periods (Above Avg Load)")
st.pyplot(fig4)
