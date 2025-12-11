"""
Sample data generators for EducationPeople MEAL demo.
These functions let the Streamlit app load demo datasets even if no files are uploaded.

Used by:
 - Logframe Mapping page
 - Org Dashboard page
"""

import pandas as pd


def demo_logframe() -> pd.DataFrame:
    """Create a built-in demo logframe simulating 5 sample projects."""
    data = {
        "Project": [
            "Project A – Remedial Learning",
            "Project A – Remedial Learning",
            "Project B – Infrastructure Support",
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


def demo_mapping() -> pd.DataFrame:
    """Create a dataset that simulates output from the AI mapping engine."""
    data = {
        "Project": [
            "Project A – Remedial Learning",
            "Project A – Remedial Learning",
            "Project B – Infrastructure Support",
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


def save_demo_files(path="data/sample_logframes"):
    """Creates CSV files in the repo (optional helper)."""
    import os

    os.makedirs(path, exist_ok=True)

    demo_logframe().to_csv(f"{path}/demo_logframe.csv", index=False)
    demo_mapping().to_csv(f"{path}/demo_mapping.csv", index=False)

    return {
        "logframe_file": f"{path}/demo_logframe.csv",
        "mapping_file": f"{path}/demo_mapping.csv",
    }

