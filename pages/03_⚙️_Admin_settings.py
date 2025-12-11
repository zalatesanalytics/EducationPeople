import streamlit as st

st.title("⚙️ Admin & Configuration")

st.markdown(
    """
This page is the **admin/configuration** placeholder for the EducationPeople MEAL system.

Planned features for this space:

- Configure **data sources**  
  - KoboToolbox forms and API tokens  
  - SurveyMonkey surveys and mappings  
  - Excel upload rules (naming conventions, templates)  

- Manage **EducationPeople organizational indicator dictionary**  
  - Add / edit indicators  
  - Activate / deactivate indicators  
  - Map indicators to strategic outcomes  

- Run **data quality checks**  
  - Gender completeness (Female + Male = Total)  
  - Missing or outlier values  
  - Duplicate records across projects  

- Configure **user roles & access levels**  
  - MEAL staff, program managers, partners, donors  

For now, this page documents the roadmap and shows that the system is
designed to be **scalable, multi-project, and gender-responsive**.
"""
)
