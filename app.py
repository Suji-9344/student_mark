import streamlit as st
import pandas as pd

st.set_page_config(page_title="Marks Increase / Decrease", layout="wide")
st.title("📊 Student Marks Increase / Decrease Analysis")

# ---------- USER INPUT ----------
st.sidebar.header("🔧 Student Input")

student_name = st.sidebar.text_input("Student Name", "Aarav")

start_year = st.sidebar.number_input(
    "Starting Academic Year",
    min_value=2000,
    max_value=2100,
    value=2010
)

num_years = st.sidebar.slider(
    "Number of Academic Years",
    5, 50, 10
)

first_year_marks = st.sidebar.slider(
    "Marks in First Year",
    0, 100, 60
)

# ---------- GENERATE DATA ----------
academic_years = []
marks_list = []

marks = first_year_marks

for i in range(num_years):
    year = start_year + i
    academic_years.append(f"{year}-{year+1}")

    # Increase / Decrease logic
    if i == 0:
        marks = first_year_marks
    elif i % 2 == 0:
        marks = min(100, marks + 5)   # increase
    else:
        marks = max(0, marks - 3)     # decrease

    marks_list.append(marks)

df = pd.DataFrame({
    "Student_Name": student_name,
    "Academic_Year": academic_years,
    "Marks": marks_list
})

# ---------- CALCULATE CHANGE ----------
df["Change"] = df["Marks"].diff()
df["Result"] = df["Change"].apply(
    lambda x: "⬆ Increase" if x > 0 else ("⬇ Decrease" if x < 0 else "➖ No Change")
)

# ---------- DISPLAY ----------
st.subheader("📄 Year-wise Marks")
st.dataframe(df, use_container_width=True)

# ---------- YEAR SELECTION ----------
selected_year = st.selectbox(
    "📌 Select Academic Year to See Result",
    df["Academic_Year"]
)

row = df[df["Academic_Year"] == selected_year].iloc[0]

st.subheader("📢 Selected Year Result")
st.write("**Academic Year:**", selected_year)
st.write("**Marks:**", row["Marks"])
st.write("**Status:**", row["Result"])

# ---------- GRAPH ----------
df["Year_Start"] = df["Academic_Year"].str.split("-").str[0].astype(int)

st.subheader("📈 Marks Trend")
st.line_chart(df.set_index("Year_Start")["Marks"])
