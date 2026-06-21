import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="AI Predictive Maintenance System",
    page_icon="🖥️",
    layout="wide"
)

# Load Data
df = pd.read_csv("data/system_metrics.csv")
latest = df.iloc[-1]

# Title
st.title("🖥️ AI-Based Predictive Maintenance System")
st.caption("Real-Time Monitoring for Personal Computers and Data Centers")

st.write(
    "This system collects live telemetry from a computer, stores historical "
    "metrics, and will use machine learning to predict hardware deterioration "
    "and maintenance risks."
)

# Dataset Statistics
st.subheader("📊 Dataset Statistics")
st.write(f"Total Records Collected: {len(df)}")

# Health Status
if latest["cpu_usage"] < 70:
    st.success("🟢 System Status: SAFE")

elif latest["cpu_usage"] < 90:
    st.warning("🟡 System Status: WARNING")

else:
    st.error("🔴 System Status: CRITICAL")

# Current Status
st.subheader("⚡ Current System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{latest['cpu_usage']} %")

with col2:
    st.metric("RAM Usage", f"{latest['ram_usage']} %")

with col3:
    st.metric("Disk Usage", f"{latest['disk_usage']} %")

# Machine Information
st.subheader("🖥️ Machine Information")

info1, info2, info3 = st.columns(3)

with info1:
    st.metric("CPU Cores", latest["cpu_cores"])

with info2:
    st.metric("Total RAM (GB)", latest["total_ram_gb"])

with info3:
    st.metric("Machine Name", latest["machine_name"])

# AI Section Placeholder
st.subheader("🤖 AI Prediction Module")
st.info("Machine Learning prediction system will be added after sufficient telemetry data is collected.")

# Graphs
st.subheader("📈 CPU Usage Over Time")
st.line_chart(df["cpu_usage"])

st.subheader("📈 RAM Usage Over Time")
st.line_chart(df["ram_usage"])

st.subheader("📈 CPU Frequency Over Time")
st.line_chart(df["cpu_frequency"])

st.subheader("📈 Disk Usage Over Time")
st.line_chart(df["disk_usage"])

# Raw Data
with st.expander("📄 View Raw Telemetry Data"):
    st.dataframe(df)