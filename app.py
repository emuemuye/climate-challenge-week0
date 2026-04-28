import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🌍 Ethiopia Climate Dashboard")

# Load data
df = pd.read_csv("data/ethiopia_clean.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# ----------------------------
# TEMPERATURE TREND
# ----------------------------
st.subheader("🌡 Temperature Trend")

temp = df.groupby("date")["T2M"].mean()

fig, ax = plt.subplots()
temp.plot(ax=ax)
ax.set_title("Temperature Over Time")
st.pyplot(fig)

# ----------------------------
# RAINFALL
# ----------------------------
st.subheader("🌧 Rainfall Pattern")

df["month"] = df["date"].dt.month
rain = df.groupby("month")["PRECTOTCORR"].mean()

fig, ax = plt.subplots()
rain.plot(kind="bar", ax=ax)
ax.set_title("Monthly Rainfall")
st.pyplot(fig)

st.subheader("🔥 Extreme Heat Days")

threshold = df["T2M_MAX"].quantile(0.9)
extreme = df[df["T2M_MAX"] > threshold]

fig, ax = plt.subplots()
extreme.groupby("month").size().plot(kind="bar", ax=ax)
ax.set_title("Extreme Heat Events")
st.pyplot(fig)
