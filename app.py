import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Student Academic Performance", layout="wide")
st.title("📊 One Student – Academic Year Marks Analysis")

FILE_NAME = "one_student_200_academic_year_marks.xlsx"

def generate_data():
    data = {
        "Student_ID": [1] * 200,
        "Student_Name": ["Aarav"] * 200,
        "Academic_Year": [f"{1825+i}-{1826+i}" for i in range(200)],
        "Marks": [(50 + i) % 100 for i in range(200)]
    }
    df = pd.DataFrame(data)
    df.to_excel(FILE_NAME, index=False)
    return df

# Load or create dataset automatically
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = generate_data()

# Show data
st.subheader("📄 Student Academic Data")
st.dataframe(df, use_container_width=True)

# Prepare year for plotting
df["Year_Start"] = df["Academic_Year"].astype(str).str.split("-").str[0].astype(int)

# Plot
st.subheader("📈 Academic Year vs Marks")
st.line_chart(df.set_index("Year_Start")["Marks"])

# Summary
st.subheader("📌 Performance Summary")
st.write("**Student Name:**", df["Student_Name"].iloc[0])
st.write("**Total Academic Years:**", len(df))
st.write("**Average Marks:**", round(df["Marks"].mean(), 2))
st.write("**Highest Marks:**", df["Marks"].max())
st.write("**Lowest Marks:**", df["Marks"].min())
