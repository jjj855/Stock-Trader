# app.py
import streamlit as st
from src.fetch_trades import fetch_trades
from src.analyzer import whale_score, confidence_score
from src.visualizer import plot_top_traded

data = fetch_trades(api_key="YOUR_API_KEY")
st.title("Politician Stock Trade Suggester")

# Filters
min_conf = st.slider("Min Confidence Score", 0, 10, 3)
selected_data = [t for t in data if confidence_score([t]) >= min_conf]

# Graph
plot_top_traded(selected_data)

# Table
for t in selected_data[:10]:
    st.write(f"{t['Ticker']}: Whale={whale_score(t)}, Confidence={confidence_score([t])}")
