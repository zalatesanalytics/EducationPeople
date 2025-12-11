import streamlit as st
import pandas as pd

from src.indicator_catalog import EDUCATIONPEOPLE_INDICATORS
from src.dashboard_utils import run_dashboard_with_gender


st.title("📈 EducationPeople – Organizational Dashboard")

st.write(
    """
Upload a dataset that includes:

- Project indicator names
- Mapped organizational indicator IDs
- Reported values and (optionally) gender-disaggregated values

Or use the built-in demo dataset to see how the dashboard works.
"""
)


def make_demo_mapping_df() -> pd.DataFrame:
    data = {
        "Project": [
            "Project A – Remedial Learning",
            "Project A – Remedial Learning",
            "Project B – School Infrastructure",
            "Project C – Teacher Training",
            "Project D – Reading Promotion",
            "Project E – Community Engagement",
        ],
        "Project_Indicator_Name": [
            "Number of students attending remedial classes",
            "Number of students receiving learning support at school",
            "Number of schools with improved classrooms",
            "Number of teachers trained in active pedagogy",
            "Number of reading books distributed to students",
            "Number of households engaged in parenting sessions",
        ],
        "Mapped_Org_Indicator_ID": [
            "EDP_OUT1_STUD",
            "EDP_OUT1_STUD",
            "EDP_OUT1_SCH",
            "EDP_OUT1_TCH",
            "EDP_OUT1_BKS",
            "EDP_OUT2_HH",
        ],
        "Reported_Value": [1200, 800, 25, 160, 5000, 900],
        "Female_Value": [700, 480, 0, 90, 2600, 600],
        "Male_Value": [500, 320, 0, 70, 2400, 300],
    }
    return pd.DataFrame(data)


uploaded_file = st.file_uploader(
    "Upload mapping + values data (CSV/Excel):",
    type=["xlsx", "xls", "csv"],
    accept_multiple_files=False,
)

use_demo = st.checkbox(
    "Use built-in demo mapping dataset",
    value=not uploaded_file,
)

if use_demo:
    df = make_demo_mapping_df()
    st.info("Using built-in demo dataset.")
elif uploaded_file:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame()

if not df.empty:
    st.subheader("Input data preview")
    st.dataframe(df.head(20), use_container_width=True)

    run_dashboard_with_gender(
        df,
        org_indicators=EDUCATIONPEOPLE_INDICATORS,
        indicator_col="Project_Indicator_Name",
        org_indicator_col="Mapped_Org_Indicator_ID",
        project_col="Project",
    )
else:
    st.info("Upload a file or enable the demo dataset to view the dashboard.")
