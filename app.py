import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Page config
st.set_page_config(page_title="Stock Price Dashboard", layout="wide")

st.title("📈 Stock Price Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("stock_hk.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Sidebar controls
st.sidebar.header("🔍 Filters")

# Stock selection
stock_list = df["Stock"].unique()
selected_stock = st.sidebar.selectbox("Select Stock", stock_list)

# Filter stock
stock_df = df[df["Stock"] == selected_stock]

# Date range
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [stock_df.Date.min(), stock_df.Date.max()]
)

# Filter by date
filtered_df = stock_df[
    (stock_df.Date >= pd.to_datetime(start_date)) &
    (stock_df.Date <= pd.to_datetime(end_date))
]

# Price column selection
price_col = st.sidebar.selectbox(
    "Select Price Type",
    ["Open", "High", "Low", "Close"]
)

# Plot
st.subheader(f"📊 {selected_stock} - {price_col} Price Trend")

fig, ax = plt.subplots(figsize=(12, 5))
sb.lineplot(data=filtered_df, x="Date", y=price_col, ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.grid(True)

st.pyplot(fig)

# Show raw data (optional)
with st.expander("📄 View Raw Data"):
    st.dataframe(filtered_df)
