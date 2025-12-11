import streamlit as st

st.set_page_config(
    page_title="EducationPeople – MEAL Suite by Zalates Analytics",
    layout="wide",
    page_icon="📊",
)

st.title("📊 EducationPeople – Integrated MEAL Suite")

st.markdown(
    """
Welcome to the **EducationPeople MEAL dashboard**, built by **Zalates Analytics**.

Use the sidebar to navigate between:

- **📑 Logframe mapping** – upload or use demo project logframes and map them to EducationPeople organizational indicators  
- **📈 Org dashboard** – see aggregated results (with gender disaggregation)  
- **⚙️ Admin settings** – configuration roadmap and notes  

This is a working prototype that you can plug into:

- KoboToolbox  
- SurveyMonkey  
- Excel/CSV partner reports  
"""
)
