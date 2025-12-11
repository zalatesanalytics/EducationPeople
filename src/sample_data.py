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
import numpy as np

# -------------------------------------------------------------------
# Random synthetic project data generator for large test datasets
# -------------------------------------------------------------------

PROGRAM_TYPES = [
    "Remedial Learning",
    "School Infrastructure",
    "Teacher Training",
    "Reading Promotion",
    "Community Engagement",
    "Parenting Support",
    "School Governance",
]

FOCUS_AREAS = [
    "Literacy",
    "Numeracy",
    "STEM",
    "Social Emotional Learning",
    "Inclusive Education",
    "Gender Equality",
    "Child Protection",
]

ORG_INDICATOR_IDS = [
    "EDP_OUT1_STUD",  # students
    "EDP_OUT1_SCH",   # schools
    "EDP_OUT1_TCH",   # teachers
    "EDP_OUT1_BKS",   # books
    "EDP_OUT2_HH",    # households
]


def _indicator_name_for_org_id(org_id: str) -> str:
    """Helper to generate a realistic indicator name text."""
    mapping = {
        "EDP_OUT1_STUD": [
            "Number of students reached through project activities",
            "Number of learners attending remedial or support classes",
        ],
        "EDP_OUT1_SCH": [
            "Number of schools supported with EducationPeople services",
            "Number of schools with improved learning environments",
        ],
        "EDP_OUT1_TCH": [
            "Number of teachers trained in active pedagogy",
            "Number of teachers reached with CPD sessions",
        ],
        "EDP_OUT1_BKS": [
            "Number of reading books distributed to students",
            "Number of learning materials distributed to schools",
        ],
        "EDP_OUT2_HH": [
            "Number of households engaged in education support",
            "Number of caregivers participating in parenting sessions",
        ],
    }
    choices = mapping.get(org_id, ["Project indicator related to education outcomes"])
    return np.random.choice(choices)


def generate_random_projects_data(
    num_rows: int = 1000,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Generate a large random dataset of project indicator rows across:
    - The EducationPeople countries
    - Different projects / programs / focus areas
    - Different org indicator IDs

    Each row ~ one indicator value for a country / project / school.
    """
    rng = np.random.default_rng(seed)

    countries = COUNTRIES  # from above in this file

    regions = {
        "Kenya": ["Nairobi County", "Mombasa", "Kisumu"],
        "Tanzania": ["Dar es Salaam", "Mwanza"],
        "Rwanda": ["Kigali City", "Eastern Province"],
        "Mozambique": ["Nampula", "Zambezia"],
        "Liberia": ["Montserrado", "Grand Bassa"],
        "Libya": ["Tripoli District", "Benghazi District"],
        "Angola": ["Luanda Province", "Huambo"],
        "Honduras": ["Cortés", "Francisco Morazán"],
        "El Salvador": ["San Salvador", "Santa Ana"],
        "Sri Lanka": ["Western Province", "Central Province"],
        "Vietnam": ["Ho Chi Minh City", "Hanoi"],
    }

    projects = [
        "Project A – Remedial Learning",
        "Project B – Infrastructure Support",
        "Project C – Teacher Training",
        "Project D – Reading Promotion",
        "Project E – Community Engagement",
        "Project F – Parenting & Governance",
    ]

    rows = []
    for i in range(num_rows):
        country = rng.choice(countries)
        region = rng.choice(regions[country])
        district = f"District {rng.integers(1, 6)}"
        school = f"{region} Community School {rng.integers(1, 10)}"
        project = rng.choice(projects)
        program_type = rng.choice(PROGRAM_TYPES)
        focus_area = rng.choice(FOCUS_AREAS)
        org_id = rng.choice(ORG_INDICATOR_IDS)

        # Generate indicator text related to that org ID
        indicator_text = _indicator_name_for_org_id(org_id)

        # Values: bigger for students/books, smaller for schools/teachers/households
        base = {
            "EDP_OUT1_STUD": rng.integers(50, 800),
            "EDP_OUT1_SCH": rng.integers(1, 20),
            "EDP_OUT1_TCH": rng.integers(5, 200),
            "EDP_OUT1_BKS": rng.integers(200, 10000),
            "EDP_OUT2_HH": rng.integers(20, 1000),
        }[org_id]

        # Add some noise and gender split
        reported_value = int(base + rng.normal(0, base * 0.1))
        reported_value = max(reported_value, 0)

        female_share = rng.uniform(0.45, 0.6)
        female_value = int(reported_value * female_share)
        male_value = reported_value - female_value

        rows.append(
            {
                "Project": project,
                "Country": country,
                "Region": region,
                "District": district,
                "School_Name": school,
                "Program_Type": program_type,
                "Focus_Area": focus_area,
                "Project_Indicator_Name": indicator_text,
                "Mapped_Org_Indicator_ID": org_id,
                "Reported_Value": reported_value,
                "Female_Value": female_value,
                "Male_Value": male_value,
            }
        )

    df = pd.DataFrame(rows)
    return df


def save_random_project_files(
    path: str = "data/random_inputs",
    n_files: int = 3,
    rows_per_file: int = 400,
    seed: int = 123,
):
    """
    Generate multiple random input files that you can upload to the app.
    Each file has rows_per_file >= 300 (default 400).
    """
    import os

    os.makedirs(path, exist_ok=True)

    rng = np.random.default_rng(seed)
    file_paths = []

    for i in range(n_files):
        df = generate_random_projects_data(
            num_rows=rows_per_file,
            seed=int(seed + i * 10),
        )
        csv_path = os.path.join(path, f"random_project_data_{i+1}.csv")
        df.to_csv(csv_path, index=False)
        file_paths.append(csv_path)

    return file_paths
