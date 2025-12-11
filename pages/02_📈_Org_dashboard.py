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

Use the sidebar to filter by **Country** and **Project**.
"""
)

# -------- Data selection (demo vs upload) --------
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
    df = demo_mapping()
    st.info("Using built-in demo mapping dataset.")
elif uploaded_file:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame()

# -------- Sidebar filters: Country & Project --------
if not df.empty:
    with st.sidebar:
        st.markdown("### 🌍 Filters")

        filt_df = df.copy()

        # Country filter
        if "Country" in filt_df.columns:
            countries = sorted(filt_df["Country"].dropna().unique())
            selected_countries = st.multiselect(
                "Country",
                options=countries,
                default=countries,
            )
            if selected_countries:
                filt_df = filt_df[filt_df["Country"].isin(selected_countries)]

        # Project filter
        if "Project" in filt_df.columns:
            projects = sorted(filt_df["Project"].dropna().unique())
            selected_projects = st.multiselect(
                "Project",
                options=projects,
                default=projects,
            )
            if selected_projects:
                filt_df = filt_df[filt_df["Project"].isin(selected_projects)]

    st.subheader("Filtered data preview")
    st.dataframe(filt_df.head(20), use_container_width=True)

    if filt_df.empty:
        st.warning("No data after applying filters. Try selecting more countries/projects.")
    else:
        run_dashboard_with_gender(
            filt_df,
            org_indicators=EDUCATIONPEOPLE_INDICATORS,
            indicator_col="Project_Indicator_Name",
            org_indicator_col="Mapped_Org_Indicator_ID",
            project_col="Project",
            country_col="Country",
        )
else:
    st.info("Upload a file or enable the demo dataset to view the dashboard.")
