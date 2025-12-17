import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Student Academic Performance", layout="wide")

st.title("📊 One Student – Academic Year Marks Analysis")

# Load Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("one_student_200_academic_year_marks.xlsx")
    return df

try:
    df = load_data()

    # Show dataset
    st.subheader("📄 Student Academic Data")
    st.dataframe(df)

    # Convert Academic Year for plotting
    df["Year_Start"] = df["Academic_Year"].str.split("-").str[0].astype(int)

    # Line chart
    st.subheader("📈 Academic Year vs Marks")
    st.line_chart(
        data=df,
        x="Year_Start",
        y="Marks"
    )

    # Summary
    st.subheader("📌 Performance Summary")
    st.write("**Student Name:**", df["Student_Name"].iloc[0])
    st.write("**Total Academic Years:**", len(df))
    st.write("**Average Marks:**", round(df["Marks"].mean(), 2))
    st.write("**Highest Marks:**", df["Marks"].max())
    st.write("**Lowest Marks:**", df["Marks"].min())

except FileNotFoundError:
    st.error("❌ Excel file not found. Please upload 'one_student_200_academic_year_marks.xlsx' to the project folder.")
