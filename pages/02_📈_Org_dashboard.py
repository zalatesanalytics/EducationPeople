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

You can also filter by **country, region, district, school, and project**
to compare performance across locations and interventions.
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

# -------- Subnational & project filters --------
if not df.empty:
    st.subheader("Filters")

    # Work on a copy so original df isn't destroyed
    filt_df = df.copy()

    # Sidebar or top filters? Let's use the sidebar to save space.
    with st.sidebar:
        st.markdown("### 🌍 Location & Project Filters")

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

        # Region filter
        if "Region" in filt_df.columns:
            regions = sorted(filt_df["Region"].dropna().unique())
            selected_regions = st.multiselect(
                "Region",
                options=regions,
                default=regions,
            )
            if selected_regions:
                filt_df = filt_df[filt_df["Region"].isin(selected_regions)]

        # District filter
        if "District" in filt_df.columns:
            districts = sorted(filt_df["District"].dropna().unique())
            selected_districts = st.multiselect(
                "District",
                options=districts,
                default=districts,
            )
            if selected_districts:
                filt_df = filt_df[filt_df["District"].isin(selected_districts)]

        # School filter
        # (column may be School_Name or School; use whichever exists)
        school_col = None
        if "School_Name" in filt_df.columns:
            school_col = "School_Name"
        elif "School" in filt_df.columns:
            school_col = "School"

        if school_col is not None:
            schools = sorted(filt_df[school_col].dropna().unique())
            selected_schools = st.multiselect(
                "School",
                options=schools,
                default=schools,
            )
            if selected_schools:
                filt_df = filt_df[filt_df[school_col].isin(selected_schools)]

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

    # Show preview of filtered data
    st.subheader("Filtered data preview")
    st.dataframe(filt_df.head(20), use_container_width=True)

    if filt_df.empty:
        st.warning("No data after applying filters. Try selecting more locations/projects.")
    else:
        # Run the dashboard with filtered data
        run_dashboard_with_gender(
            filt_df,
            org_indicators=EDUCATIONPEOPLE_INDICATORS,
            indicator_col="Project_Indicator_Name",
            org_indicator_col="Mapped_Org_Indicator_ID",
            project_col="Project",
        )
else:
    st.info("Upload a file or enable the demo dataset to view the dashboard.")
