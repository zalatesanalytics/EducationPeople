import streamlit as st
import pandas as pd

from src.indicator_catalog import EDUCATIONPEOPLE_INDICATORS
from src.dashboard_utils import run_dashboard_with_gender
from src.sample_data import demo_mapping


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

uploaded_file = st.file_uploader(
    "Upload mapping + values data (CSV/Excel):",
    type=["xlsx", "xls", "csv"],
    accept_multiple_files=False,
)

use_demo = st.checkbox(
    "Use built-in demo mapping dataset",
    value=not uploaded_file,
)

# --- Load data: demo or uploaded ---
if use_demo:
    df = demo_mapping()
    st.info("Using built-in demo mapping dataset.")
elif uploaded_file:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame()

# --- Show dashboard ---
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
