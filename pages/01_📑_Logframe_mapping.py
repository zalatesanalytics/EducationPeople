import streamlit as st
import pandas as pd

from src.indicator_catalog import EDUCATIONPEOPLE_INDICATORS
from src.mapping_engine import map_indicator_to_org


st.title("📑 Logframe Mapping – Project → EducationPeople")

st.write(
    """
Upload project logframes (Excel/CSV) or use the built-in demo data.
The AI-style mapping engine will propose which EducationPeople
organizational indicator each project indicator contributes to.
"""
)


def make_demo_logframe() -> pd.DataFrame:
    data = {
        "Project": [
            "Project A – Remedial Learning",
            "Project A – Remedial Learning",
            "Project B – School Infrastructure",
            "Project C – Teacher Training",
            "Project D – Reading Promotion",
            "Project E – Community Engagement",
        ],
        "Indicator_Name": [
            "Number of students attending remedial classes",
            "Number of students receiving learning support at school",
            "Number of schools with improved classrooms",
            "Number of teachers trained in active pedagogy",
            "Number of reading books distributed to students",
            "Number of households engaged in parenting sessions",
        ],
        "Level": [
            "Outcome",
            "Outcome",
            "Output",
            "Output",
            "Output",
            "Output",
        ],
        "Reported_Value": [1200, 800, 25, 160, 5000, 900],
        "Female_Value": [700, 480, 0, 90, 2600, 600],
        "Male_Value": [500, 320, 0, 70, 2400, 300],
    }
    return pd.DataFrame(data)


uploaded_files = st.file_uploader(
    "Upload one or more logframe files (Excel/CSV):",
    type=["xlsx", "xls", "csv"],
    accept_multiple_files=True,
)

use_demo = st.checkbox(
    "Use built-in demo logframe (EducationPeople sample projects)",
    value=not uploaded_files,
)

indicator_col = st.text_input("Column containing indicator text:", value="Indicator_Name")
project_col = st.text_input("Column containing project name:", value="Project")
threshold = st.slider("Similarity threshold", 0.3, 0.9, 0.5, 0.05)

if use_demo:
    logframes_df = make_demo_logframe()
    st.info("Showing built-in demo logframe.")
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

    logframes_df = pd.concat(dfs, ignore_index=True)
else:
    logframes_df = pd.DataFrame()

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
                    "Project_Indicator_Name": text,
                    "Mapped_Org_Indicator_ID": org_id,
                    "Similarity_Score": score,
                    "Reported_Value": row.get("Reported_Value", None),
                    "Female_Value": row.get("Female_Value", None),
                    "Male_Value": row.get("Male_Value", None),
                }
            )

        mapping_df = pd.DataFrame(mapping_records)

        st.subheader("AI mapping results")
        st.dataframe(mapping_df, use_container_width=True)

        st.download_button(
            "⬇️ Download mapping as CSV (for dashboard page)",
            data=mapping_df.to_csv(index=False),
            file_name="educationpeople_mapping_demo.csv",
            mime="text/csv",
        )
else:
    st.info("Upload logframes or enable the demo logframe to see mappings.")
