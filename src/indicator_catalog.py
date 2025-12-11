"""
Indicator catalog for EducationPeople.

Later this can be loaded from a database or CSV.
"""

EDUCATIONPEOPLE_INDICATORS = [
    {
        "org_indicator_id": "EDP_OUT1_STUD",
        "name": "Number of students reached",
        "description": "Total unique learners participating in EducationPeople-supported interventions",
        "level": "Outcome",
        "unit": "Learners",
        "disaggregation": "Sex, age, location",
    },
    {
        "org_indicator_id": "EDP_OUT1_SCH",
        "name": "Number of schools supported",
        "description": "Schools receiving any form of support from EducationPeople projects",
        "level": "Output",
        "unit": "Schools",
        "disaggregation": "Location, school type",
    },
    {
        "org_indicator_id": "EDP_OUT1_TCH",
        "name": "Number of teachers trained",
        "description": "Teachers who completed EducationPeople-supported capacity building",
        "level": "Output",
        "unit": "Teachers",
        "disaggregation": "Sex, grade level, subject",
    },
    {
        "org_indicator_id": "EDP_OUT1_BKS",
        "name": "Number of books distributed",
        "description": "Learning materials and books distributed to learners or schools",
        "level": "Output",
        "unit": "Books",
        "disaggregation": "Grade level, subject",
    },
    {
        "org_indicator_id": "EDP_OUT1_CLS",
        "name": "Number of classrooms built or renovated",
        "description": "Physical learning spaces constructed or upgraded through EducationPeople projects",
        "level": "Output",
        "unit": "Classrooms",
        "disaggregation": "Location, level",
    },
    {
        "org_indicator_id": "EDP_OUT2_HH",
        "name": "Number of households engaged in education support",
        "description": "Households participating in school-community engagement activities",
        "level": "Output",
        "unit": "Households",
        "disaggregation": "Sex of household head, location",
    },
]
