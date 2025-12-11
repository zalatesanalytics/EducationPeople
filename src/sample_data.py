"""
Sample data generators for EducationPeople MEAL demo.
These functions let the Streamlit app load demo datasets even if no files are uploaded.

Used by:
 - Logframe Mapping page
 - Org Dashboard page
"""

import pandas as pd


COUNTRIES = [
    "Kenya",
    "Tanzania",
    "Rwanda",
    "Mozambique",
    "Liberia",
    "Libya",
    "Angola",
    "Honduras",
    "El Salvador",
    "Sri Lanka",
    "Vietnam",
]


def demo_logframe() -> pd.DataFrame:
    """Create a built-in demo logframe with the requested countries."""
    data = {
        "Project": [
            "Project KE – Remedial Learning",
            "Project TZ – School Infrastructure",
            "Project RW – Teacher Training",
            "Project MZ – Reading Promotion",
            "Project LR – Community Engagement",
            "Project LY – Remedial Learning",
            "Project AO – School Infrastructure",
            "Project HN – Teacher Training",
            "Project SV – Reading Promotion",
            "Project LK – Community Engagement",
            "Project VN – Remedial Learning",
        ],
        "Country": [
            "Kenya",
            "Tanzania",
            "Rwanda",
            "Mozambique",
            "Liberia",
            "Libya",
            "Angola",
            "Honduras",
            "El Salvador",
            "Sri Lanka",
            "Vietnam",
        ],
        "Region": [
            "Nairobi County",
            "Dar es Salaam",
            "Kigali City",
            "Nampula",
            "Montserrado",
            "Tripoli District",
            "Luanda Province",
            "Cortés",
            "San Salvador",
            "Western Province",
            "Ho Chi Minh City",
        ],
        "District": [
            "Kasarani",
            "Kinondoni",
            "Gasabo",
            "Nampula City",
            "Monrovia",
            "Tripoli",
            "Luanda",
            "San Pedro Sula",
            "San Salvador Centro",
            "Colombo-like",
            "District 1",
        ],
        "School_Name": [
            "Kasarani Model School",
            "Kinondoni Primary School",
            "Gasabo Community School",
            "Nampula Reading Centre",
            "Monrovia Community School",
            "Tripoli Learning Centre",
            "Luanda Model School",
            "San Pedro Learning Hub",
            "San Salvador Reading Centre",
            "Colombo Education Centre",
            "District 1 Community School",
        ],
        "Indicator_Name": [
            "Number of students attending remedial classes",
            "Number of schools with improved classrooms",
            "Number of teachers trained in active pedagogy",
            "Number of reading books distributed to students",
            "Number of households engaged in parenting sessions",
            "Number of students receiving learning support at school",
            "Number of schools supported with learning materials",
            "Number of teachers trained on inclusive pedagogy",
            "Number of reading books distributed to households",
            "Number of households engaged in school governance",
            "Number of students attending remedial classes",
        ],
        "Level": [
            "Outcome",
            "Output",
            "Output",
            "Output",
            "Output",
            "Outcome",
            "Output",
            "Output",
            "Output",
            "Output",
            "Outcome",
        ],
        "Reported_Value": [1200, 30, 80, 6000, 900, 1000, 25, 70, 4500, 800, 1500],
        "Female_Value":   [700,  0, 45, 3200, 600,  580,  0, 40, 2400, 520,  900],
        "Male_Value":     [500,  0, 35, 2800, 300,  420,  0, 30, 2100, 280,  600],
    }
    return pd.DataFrame(data)


def demo_mapping() -> pd.DataFrame:
    """Create a dataset that simulates output from the AI mapping engine, with subnational info."""
    data = {
        "Project": [
            "Project KE – Remedial Learning",
            "Project TZ – School Infrastructure",
            "Project RW – Teacher Training",
            "Project MZ – Reading Promotion",
            "Project LR – Community Engagement",
            "Project LY – Remedial Learning",
            "Project AO – School Infrastructure",
            "Project HN – Teacher Training",
            "Project SV – Reading Promotion",
            "Project LK – Community Engagement",
            "Project VN – Remedial Learning",
        ],
        "Country": [
            "Kenya",
            "Tanzania",
            "Rwanda",
            "Mozambique",
            "Liberia",
            "Libya",
            "Angola",
            "Honduras",
            "El Salvador",
            "Sri Lanka",
            "Vietnam",
        ],
        "Region": [
            "Nairobi County",
            "Dar es Salaam",
            "Kigali City",
            "Nampula",
            "Montserrado",
            "Tripoli District",
            "Luanda Province",
            "Cortés",
            "San Salvador",
            "Western Province",
            "Ho Chi Minh City",
        ],
        "District": [
            "Kasarani",
            "Kinondoni",
            "Gasabo",
            "Nampula City",
            "Monrovia",
            "Tripoli",
            "Luanda",
            "San Pedro Sula",
            "San Salvador Centro",
            "Colombo-like",
            "District 1",
        ],
        "School_Name": [
            "Kasarani Model School",
            "Kinondoni Primary School",
            "Gasabo Community School",
            "Nampula Reading Centre",
            "Monrovia Community School",
            "Tripoli Learning Centre",
            "Luanda Model School",
            "San Pedro Learning Hub",
            "San Salvador Reading Centre",
            "Colombo Education Centre",
            "District 1 Community School",
        ],
        "Project_Indicator_Name": [
            "Number of students attending remedial classes",
            "Number of schools with improved classrooms",
            "Number of teachers trained in active pedagogy",
            "Number of reading books distributed to students",
            "Number of households engaged in parenting sessions",
            "Number of students receiving learning support at school",
            "Number of schools supported with learning materials",
            "Number of teachers trained on inclusive pedagogy",
            "Number of reading books distributed to households",
            "Number of households engaged in school governance",
            "Number of students attending remedial classes",
        ],
        "Mapped_Org_Indicator_ID": [
            "EDP_OUT1_STUD",  # Kenya – students
            "EDP_OUT1_SCH",   # Tanzania – schools
            "EDP_OUT1_TCH",   # Rwanda – teachers
            "EDP_OUT1_BKS",   # Mozambique – books
            "EDP_OUT2_HH",    # Liberia – households
            "EDP_OUT1_STUD",  # Libya – students
            "EDP_OUT1_SCH",   # Angola – schools
            "EDP_OUT1_TCH",   # Honduras – teachers
            "EDP_OUT1_BKS",   # El Salvador – books
            "EDP_OUT2_HH",    # Sri Lanka – households
            "EDP_OUT1_STUD",  # Vietnam – students
        ],
        "Reported_Value": [1200, 30, 80, 6000, 900, 1000, 25, 70, 4500, 800, 1500],
        "Female_Value":   [700,  0, 45, 3200, 600,  580,  0, 40, 2400, 520,  900],
        "Male_Value":     [500,  0, 35, 2800, 300,  420,  0, 30, 2100, 280,  600],
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
