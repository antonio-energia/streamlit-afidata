#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import plotly.express as px

# --- Title ---
st.title("Simple Streamlit Test App 🧪")
st.markdown("This is a minimal app to test if Streamlit works in your environment.")

# --- Sample Data (No External Files Needed) ---
data = {
    "Year": [2025, 2026, 2027, 2028, 2029, 2030],
    "Ammonia": [1.2, 2.5, 3.1, 4.8, 5.2, 6.0],
    "Hydrogen": [0.8, 1.5, 2.3, 3.7, 4.1, 5.5],
    "Methanol": [0.5, 1.2, 1.8, 2.5, 3.0, 3.8],
}
df = pd.DataFrame(data)

# --- Sidebar Filters ---
st.sidebar.header("Filters")
selected_fuel = st.sidebar.selectbox(
    "Select Fuel Type",
    options=["Ammonia", "Hydrogen", "Methanol"]
)
start_year = st.sidebar.slider(
    "Select Start Year",
    min_value=2025,
    max_value=2030,
    value=2025
)

# --- Filter Data ---
filtered_df = df[df["Year"] >= start_year]

# --- Plot ---
st.subheader(f"Cumulative Capacity: {selected_fuel}")
fig = px.line(
    filtered_df,
    x="Year",
    y=selected_fuel,
    title=f"{selected_fuel} Capacity Over Time"
)
st.plotly_chart(fig, use_container_width=True)

# --- Data Table ---
st.subheader("Data Table")
st.dataframe(filtered_df)

# --- Success Message ---
st.success("✅ Streamlit is working! You can now customize this app.")

