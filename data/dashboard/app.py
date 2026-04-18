import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HEIST Dashboard", layout="wide")

st.title(" HEIST - Alert Fatigue System Dashboard")

# Load data
df = pd.read_csv("data/final_output.csv")


# Top Metrics

col1, col2, col3 = st.columns(3)

col1.metric("Total Logs", len(df))
col2.metric("High Risk Alerts", len(df[df["risk_level"] == "HIGH"]))
col3.metric("Unique Users", df["user"].nunique())


# Risk Distribution

st.subheader("Risk Level Distribution")

fig = px.histogram(df, x="risk_level", color="risk_level")
st.plotly_chart(fig, use_container_width=True)


#  Top Offenders

st.subheader("Top Offending IPs")

top_ips = df.groupby("ip")["risk_score"].mean().reset_index()
top_ips = top_ips.sort_values(by="risk_score", ascending=False).head(10)

st.dataframe(top_ips)


#  Risk Over Time

st.subheader("Risk Score Over Time")

df["timestamp"] = pd.to_datetime(df["timestamp"])
fig2 = px.line(df, x="timestamp", y="risk_score", color="user")

st.plotly_chart(fig2, use_container_width=True)


# Clusters

st.subheader("Alert Clusters")

fig3 = px.scatter(df, x="risk_score", y="request_count", color="cluster_id")
st.plotly_chart(fig3, use_container_width=True)