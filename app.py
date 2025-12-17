import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="📈 Time Series Marks Analysis", layout="wide")
st.title("📊 Student Marks Time Series Analysis (Using SciPy)")

# ---------------- SIDEBAR INPUT ----------------
st.sidebar.header("🔧 Enter Student Marks Over Years")

years = st.sidebar.text_input(
    "Enter Years (comma separated)",
    "2016,2017,2018,2019,2020,2021,2022,2023"
)

marks = st.sidebar.text_input(
    "Enter Marks (comma separated)",
    "64,65,66,67,68,69,70,65"
)

# ---------------- PROCESS INPUT ----------------
try:
    year_list = list(map(int, years.split(",")))
    mark_list = list(map(int, marks.split(",")))

    if len(year_list) != len(mark_list):
        st.error("❌ Number of years and marks must be the same")
        st.stop()

    df = pd.DataFrame({
        "Year": year_list,
        "Marks": mark_list
    })

    # ---------------- DISPLAY DATA ----------------
    st.subheader("📄 Time Series Data")
    st.dataframe(df)

    # ---------------- PLOT TIME SERIES ----------------
    st.subheader("📈 Marks Trend Over Time")
    fig, ax = plt.subplots()
    ax.plot(df["Year"], df["Marks"], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("Marks")
    ax.set_title("Student Marks Time Series")
    st.pyplot(fig)

    # ---------------- SCIPY TREND ANALYSIS ----------------
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["Marks"])

    st.subheader("📊 SciPy Trend Analysis Result")

    if slope > 0:
        st.success("⬆ Overall Trend: INCREASING")
    elif slope < 0:
        st.error("⬇ Overall Trend: DECREASING")
    else:
        st.info("➖ Overall Trend: NO CHANGE")

    st.write(f"**Slope:** {slope:.2f}")
    st.write(f"**Correlation (R):** {r_value:.2f}")
    st.write(f"**P-value:** {p_value:.4f}")

except Exception as e:
    st.error("❌ Please enter valid numeric values only")
