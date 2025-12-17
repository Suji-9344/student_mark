import streamlit as st
import pandas as pd

st.set_page_config(page_title="Year-wise Marks Change", layout="wide")
st.title("📊 Student Marks – Increase / Decrease Analysis")

# -------- USER INPUT --------
st.sidebar.header("🔧 Student & Year Input")

student_name = st.sidebar.text_input("Student Name", "Aarav")
start_year = st.sidebar.number_input("Starting Year", min_value=2000, max_value=2100, value=2010)
num_years = st.sidebar.slider("Number of Academic Years", 5, 50, 15)
base_marks = st.sidebar.slider("Marks in First Year", 0, 100, 60)

# -------- GENERATE DATA --------
years = []
marks = []

current_marks = base_marks

for i in range(num_years):
    year = start_year + i
    change = (-3 if i % 4 == 0 else 5)   # decrease sometimes, increase sometimes
    current_marks = max(0, min(100, current_marks + change))

    years.append(f"{year}-{year+1}")
    marks.append(current_marks)

df = pd.DataFrame({
    "Academic_Year": years,
    "Marks": marks
})

# -------- CALCULATE CHANGE --------
df["Change"] = df["Marks"].diff()
df["Status"] = df["Change"].apply(
    lambda x: "⬆ Increase" if x > 0 else ("⬇ Decrease" if x < 0 else "➖ No Change")
)

# -------- DISPLAY --------
st.subheader("📄 Academic Year Marks")
st.dataframe(df, use_container_width=True)

# -------- USER SELECT YEAR --------
selected_year = st.selectbox("📌 Select Academic Year to Check Change", df["Academic_Year"])

row = df[df["Academic_Year"] == selected_year].iloc[0]

st.subheader("📢 Result")
if pd.isna(row["Change"]):
    st.info("This is the first academic year. No previous data.")
else:
    st.write(f"**Academic Year:** {selected_year}")
    st.write(f"**Marks:** {row['Marks']}")
    st.write(f"**Change from Previous Year:** {int(row['Change'])}")
    st.write(f"**Status:** {row['Status']}")

# -------- CHART --------
df["Year_Start"] = df["Academic_Year"].str.split("-").str[0].astype(int)

st.subheader("📈 Marks Trend")
st.line_chart(df.set_index("Year_Start")["Marks"])
