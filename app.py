import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="📊 Stock Market Dashboard",
    page_icon="📈",
    layout="wide"
)

sb.set_style("whitegrid")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("stock_hk.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Dashboard Controls")

stock = st.sidebar.selectbox("📌 Select Stock", df["Stock"].unique())
price_col = st.sidebar.selectbox("💰 Price Type", ["Open", "High", "Low", "Close"])

ma20 = st.sidebar.checkbox("📈 20 Days Moving Average")
ma50 = st.sidebar.checkbox("📉 50 Days Moving Average")

stock_df = df[df["Stock"] == stock]

start_date, end_date = st.sidebar.date_input(
    "📅 Select Date Range",
    [stock_df.Date.min(), stock_df.Date.max()]
)

stock_df = stock_df[
    (stock_df.Date >= pd.to_datetime(start_date)) &
    (stock_df.Date <= pd.to_datetime(end_date))
]

# ---------------- KPI METRICS ----------------
latest = stock_df.iloc[-1]
prev = stock_df.iloc[-2] if len(stock_df) > 1 else latest

change = ((latest["Close"] - prev["Close"]) / prev["Close"]) * 100

st.title("📊 Stock Market Analysis Dashboard")

col1
