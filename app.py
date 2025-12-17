import streamlit as st

st.set_page_config(page_title="Marks Change Calculator", layout="wide")
st.title("📊 Marks Increase / Decrease Based on User Input")

# ---------- USER INPUT ----------
st.sidebar.header("🔧 Enter Two Years and Marks")

year1 = st.sidebar.number_input("Year 1", min_value=1900, max_value=2100, value=2023)
marks1 = st.sidebar.number_input("Marks in Year 1", min_value=0, max_value=100, value=60)

year2 = st.sidebar.number_input("Year 2", min_value=1900, max_value=2100, value=2024)
marks2 = st.sidebar.number_input("Marks in Year 2", min_value=0, max_value=100, value=70)

# ---------- CALCULATE CHANGE ----------
change = marks2 - marks1
percent_change = (change / marks1) * 100 if marks1 != 0 else 0

if change > 0:
    status = "⬆ Increased"
elif change < 0:
    status = "⬇ Decreased"
else:
    status = "➖ No Change"

# ---------- DISPLAY RESULT ----------
st.subheader("📌 Result Between Two Years")
st.write(f"*Year 1:* {year1}, Marks: {marks1}")
st.write(f"*Year 2:* {year2}, Marks: {marks2}")
st.write(f"*Change in Marks:* {change} ({percent_change:.2f}%)")
st.write(f"*Status:* {status}")
