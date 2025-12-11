import streamlit as st
import pandas as pd

from src.indicator_catalog import EDUCATIONPEOPLE_INDICATORS
from src.mapping_engine import map_indicator_to_org
from src.sample_data import demo_logframe


st.title("📑 Logframe Mapping – Project → EducationPeople")

st.write(
    """
Upload project logframes (Excel/CSV) or use the built-in demo data.
The AI-style mapping engine will propose which EducationPeople
organizational indicator each project indicator contributes to.
"""
)

# --- Controls ---
uploaded_files = st.file_uploader(
    "Upload one or more logframe files (Excel/CSV):",
    type=["xlsx", "xls", "csv"],
    accept_multiple_files=True,
)

use_demo = st.checkbox(
    "Use built-in demo logframe (sample EducationPeople projects)",
    value=not uploaded_files,
)

indicator_col = st.text_input("Column containing indicator text:", value="Indicator_Name")
project_col = st.text_input("Column containing project name:", value="Project")
threshold = st.slider("Similarity threshold for mapping", 0.3, 0.9, 0.5, 0.05)

# --- Load data: demo or uploaded ---
if use_demo:
    logframes_df = demo_logframe()
    logframes_df["__Source_File"] = "demo_logframe"
    st.info("Using built-in demo logframe.")
elif uploaded_files:
    dfs = []
    for f in uploaded_files:
        if f.name.lower().endswith(".csv"):
            df = pd.read_csv(f)
        else:
            df = pd.read_excel(f)

        df["__Source_File"] = f.name
        if project_col not in df.columns:
            df[project_col] = f.name
        dfs.append(df)

    if dfs:
        logframes_df = pd.concat(dfs, ignore_index=True)
    else:
        logframes_df = pd.DataFrame()
else:
    logframes_df = pd.DataFrame()

# --- Show preview & run mapping ---
if not logframes_df.empty:
    st.subheader("Combined logframes (preview)")
    st.dataframe(logframes_df.head(20), use_container_width=True)

    if indicator_col not in logframes_df.columns:
        st.error(f"Column `{indicator_col}` not found in data.")
    else:
        mapping_records = []

        for _, row in logframes_df.iterrows():
            text = str(row[indicator_col])
            org_id, score = map_indicator_to_org(
                text,
                EDUCATIONPEOPLE_INDICATORS,
                threshold=threshold,
            )
            mapping_records.append(
                {
                    "Project": row.get(project_col, "Unknown project"),
                    "Source_File": row.get("__Source_File", ""),
                    "Project_Indicator_Name": text,
                    "Mapped_Org_Indicator_ID": org_id,
                    "Similarity_Score": score,
                    "Reported_Value": row.get("Reported_Value", None),
                    "Female_Value": row.get("Female_Value", None),
                    "Male_Value": row.get("Male_Value", None),
                }
            )

        mapping_df = pd.DataFrame(mapping_records)

        st.subheader("🤖 AI mapping results")
        st.dataframe(mapping_df, use_container_width=True)

        st.download_button(
            "⬇️ Download mapping as CSV (for dashboard page)",
            data=mapping_df.to_csv(index=False),
            file_name="educationpeople_mapping.csv",
            mime="text/csv",
        )
else:
    st.info("Upload logframes or enable the demo logframe to see mappings.")
