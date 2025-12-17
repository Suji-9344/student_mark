import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Academic Performance", layout="wide")
st.title("📊 Student Academic Year Marks – User Input App")

st.sidebar.header("🔧 Enter Student Details")

# -------- USER INPUTS --------
student_name = st.sidebar.text_input("Student Name", "Aarav")
student_id = st.sidebar.number_input("Student ID", min_value=1, value=1)

num_years = st.sidebar.slider("Number of Academic Years", min_value=5, max_value=200, value=50)
start_year = st.sidebar.number_input("Starting Academic Year", min_value=1900, max_value=2100, value=2000)
start_marks = st.sidebar.slider("Starting Marks", min_value=0, max_value=100, value=50)

# -------- DATA GENERATION --------
data = {
    "Student_ID": [],
    "Student_Name": [],
    "Academic_Year": [],
    "Marks": []
}

marks = start_marks

for i in range(num_years):
    year_start = start_year + i
    year_end = year_start + 1
    academic_year = f"{year_start}-{year_end}"

    marks = min(100, marks + (i % 3))  # gradual increase

    data["Student_ID"].append(student_id)
    data["Student_Name"].append(student_name)
    data["Academic_Year"].append(academic_year)
    data["Marks"].append(marks)

df = pd.DataFrame(data)

# -------- DISPLAY DATA --------
st.subheader("📄 Student Academic Data")
st.dataframe(df, use_container_width=True)

# -------- PREPARE FOR PLOT --------
df["Year_Start"] = df["Academic_Year"].str.split("-").str[0].astype(int)

st.subheader("📈 Academic Year vs Marks")
st.line_chart(df.set_index("Year_Start")["Marks"])

# -------- SUMMARY --------
st.subheader("📌 Performance Summary")
st.write("**Student Name:**", student_name)
st.write("**Total Academic Years:**", num_years)
st.write("**Average Marks:**", round(df["Marks"].mean(), 2))
st.write("**Highest Marks:**", df["Marks"].max())
st.write("**Lowest Marks:**", df["Marks"].min())
