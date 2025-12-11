"""
Dashboard helpers for EducationPeople MEAL system.
"""

from typing import List, Dict

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def run_dashboard_with_gender(
    df: pd.DataFrame,
    org_indicators: List[Dict],
    indicator_col: str = "Project_Indicator_Name",
    org_indicator_col: str = "Mapped_Org_Indicator_ID",
    project_col: str = "Project",
    reported_col: str = "Reported_Value",
    female_col: str = "Female_Value",
    male_col: str = "Male_Value",
) -> None:
    """
    Build an org-level dashboard with optional gender disaggregation.

    Expects a DataFrame containing at least:
        - org_indicator_col (mapped org indicator ID)
        - project_col
        - indicator_col
        - reported_col (or it will be simulated)
    """

    if df.empty:
        st.info("No data provided.")
        return

    if org_indicator_col not in df.columns:
        st.error(f"Required column `{org_indicator_col}` not found in uploaded data.")
        return

    # Use or simulate a total numeric value for demonstration
    if reported_col not in df.columns:
        df[reported_col] = np.random.randint(50, 5000, size=len(df))

    df = df[df[org_indicator_col].notna()].copy()
    if df.empty:
        st.info("No mapped indicators found after filtering.")
        return

    org_df = pd.DataFrame(org_indicators)
    merged = df.merge(
        org_df[["org_indicator_id", "name"]],
        left_on=org_indicator_col,
        right_on="org_indicator_id",
        how="left",
    )

    # ----------------- Org totals (all genders) ----------------- #
    org_agg = merged.groupby([org_indicator_col, "name"], as_index=False)[reported_col].sum()
    org_agg = org_agg.rename(columns={reported_col: "Total_Value"})

    st.markdown("### 🔹 Organization-level totals (all genders combined)")
    st.dataframe(org_agg, use_container_width=True)

    fig_totals = px.bar(
        org_agg,
        x="name",
        y="Total_Value",
        title="Total by EducationPeople indicator",
    )
    fig_totals.update_layout(xaxis_title="Indicator", yaxis_title="Total")
    st.plotly_chart(fig_totals, use_container_width=True)

    # ----------------- Gender disaggregation ----------------- #
    has_female = female_col in df.columns
    has_male = male_col in df.columns

    if has_female and has_male:
        st.markdown("### 🔹 Gender-disaggregated dashboard (using real gender columns)")
        gender_df = df[[project_col, indicator_col, org_indicator_col, female_col, male_col]].copy()

        gender_df = gender_df.merge(
            org_df[["org_indicator_id", "name"]],
            left_on=org_indicator_col,
            right_on="org_indicator_id",
            how="left",
        )

        gender_df = gender_df.melt(
            id_vars=[project_col, indicator_col, org_indicator_col, "name"],
            value_vars=[female_col, male_col],
            var_name="Gender",
            value_name="Gender_Value",
        )
        gender_df["Gender"] = gender_df["Gender"].str.replace("_Value", "", regex=False)
    else:
        st.markdown("### 🔹 Gender-disaggregated dashboard (demo split from totals)")

        female_ratio, male_ratio = 0.52, 0.48

        df_f = merged.copy()
        df_f["Gender"] = "Female"
        df_f["Gender_Value"] = (df_f[reported_col] * female_ratio).round(0)

        df_m = merged.copy()
        df_m["Gender"] = "Male"
        df_m["Gender_Value"] = (df_m[reported_col] * male_ratio).round(0)

        gender_df = pd.concat([df_f, df_m], ignore_index=True)

    # org-level by gender
    org_gender_agg = gender_df.groupby([org_indicator_col, "name", "Gender"], as_index=False)[
        "Gender_Value"
    ].sum()

    st.markdown("**Organization-level totals by indicator and gender**")
    st.dataframe(org_gender_agg, use_container_width=True)

    fig_org_gender = px.bar(
        org_gender_agg,
        x="name",
        y="Gender_Value",
        color="Gender",
        barmode="group",
        title="EducationPeople indicators by gender",
    )
    fig_org_gender.update_layout(xaxis_title="Indicator", yaxis_title="Total")
    st.plotly_chart(fig_org_gender, use_container_width=True)

    # project-level by gender
    proj_gender_agg = gender_df.groupby([project_col, "name", "Gender"], as_index=False)[
        "Gender_Value"
    ].sum()

    fig_proj_gender = px.bar(
        proj_gender_agg,
        x=project_col,
        y="Gender_Value",
        color="Gender",
        facet_col="name",
        facet_col_wrap=2,
        title="Project contributions to indicators by gender",
    )
    st.plotly_chart(fig_proj_gender, use_container_width=True)
