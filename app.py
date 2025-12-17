import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Academic Performance", layout="wide")

st.title("📊 One Student – Academic Year Marks Analysis")

# Upload Excel file
uploaded_file = st.file_uploader(
    "📂 Upload Excel file (one_student_200_academic_year_marks.xlsx)",
    type=["xlsx"]
)

if uploaded_file is not None:
    # Read Excel
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 Student Academic Data")
    st.dataframe(df)

    # Extract starting year for plotting
    df["Year_Start"] = df["Academic_Year"].astype(str).str.split("-").str[0].astype(int)

    st.subheader("📈 Academic Year vs Marks")
    st.line_chart(df.set_index("Year_Start")["Marks"])

    st.subheader("📌 Performance Summary")
    st.write("**Student Name:**", df["Student_Name"].iloc[0])
    st.write("**Total Academic Years:**", len(df))
    st.write("**Average Marks:**", round(df["Marks"].mean(), 2))
    st.write("**Highest Marks:**", df["Marks"].max())
    st.write("**Lowest Marks:**", df["Marks"].min())

else:
    st.info("⬆️ Please upload the Excel file to continue")
