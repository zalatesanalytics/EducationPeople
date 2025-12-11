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
    country_col: str = "Country",
) -> None:
    """
    Build an org-level dashboard with:
      - KPI cards (students, schools, teachers, households)
      - Overall totals by org indicator
      - Distribution by country for selected indicators
      - Gender-disaggregated charts by indicator and by country
    """

    if df.empty:
        st.info("No data provided.")
        return

    # If project column is missing (e.g. aggregated uploads), create a dummy one
    if project_col not in df.columns:
        df[project_col] = "All projects"

    if org_indicator_col not in df.columns:
        st.error(f"Required column `{org_indicator_col}` not found in uploaded data.")
        return

    # Use or simulate a total numeric value for demonstration
    if reported_col not in df.columns:
        df[reported_col] = np.random.randint(50, 5000, size=len(df))

    # Only keep rows that have a mapped org indicator
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

    # ---------- KPI overview widgets (top right) ---------- #
    st.markdown("### 🔹 Key Performance Indicators")

    kpi_defs = {
        "EDP_OUT1_STUD": "Total students reached",
        "EDP_OUT1_SCH": "Total schools supported",
        "EDP_OUT1_TCH": "Total teachers trained",
        "EDP_OUT2_HH": "Total households engaged",
    }

    # Compute totals for each KPI (0 if not present)
    kpi_values = {}
    for ind_id, label in kpi_defs.items():
        value = org_agg.loc[org_agg[org_indicator_col] == ind_id, "Total_Value"].sum()
        # handle NaN
        value = 0 if pd.isna(value) else int(value)
        kpi_values[label] = value

    # Layout: empty left, KPIs on the right
    left_col, right_col = st.columns([1, 2])

    with right_col:
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)
        row1_col1.metric("👩‍🎓 Students reached", f"{kpi_values['Total students reached']:,}")
        row1_col2.metric("🏫 Schools supported", f"{kpi_values['Total schools supported']:,}")
        row2_col1.metric("👩‍🏫 Teachers trained", f"{kpi_values['Total teachers trained']:,}")
        row2_col2.metric("🏠 Households engaged", f"{kpi_values['Total households engaged']:,}")

    st.markdown("### 🔹 Organization-level totals (all indicators combined)")
    st.dataframe(org_agg, use_container_width=True)

    fig_totals = px.bar(
        org_agg,
        x="name",
        y="Total_Value",
        title="Total by EducationPeople indicator",
    )
    fig_totals.update_layout(xaxis_title="Indicator", yaxis_title="Total")
    st.plotly_chart(fig_totals, use_container_width=True)

    # ----------------- Distribution by country for selected indicators ----------------- #
    if country_col in merged.columns:
        st.markdown("### 🔹 Distribution by country for selected indicators")

        country_indicator_agg = (
            merged.groupby([country_col, org_indicator_col, "name"], as_index=False)[
                reported_col
            ].sum()
        )

        indicator_options = sorted(country_indicator_agg["name"].dropna().unique())
        selected_inds = st.multiselect(
            "Select indicators to visualize by country",
            options=indicator_options,
            default=indicator_options[: min(3, len(indicator_options))],
        )

        filt_country_ind = country_indicator_agg[
            country_indicator_agg["name"].isin(selected_inds)
        ]

        if not filt_country_ind.empty:
            fig_country = px.bar(
                filt_country_ind,
                x=country_col,
                y=reported_col,
                color="name",
                barmode="group",
                title="Distribution by country for selected indicators",
            )
            fig_country.update_layout(xaxis_title="Country", yaxis_title="Total")
            st.plotly_chart(fig_country, use_container_width=True)
        else:
            st.info("No data for the selected indicators/countries.")

    # ----------------- Gender disaggregation ----------------- #
    has_female = female_col in df.columns
    has_male = male_col in df.columns

    if has_female and has_male:
        st.markdown("### 🔹 Gender-disaggregated dashboard (using real gender columns)")

        # Decide which columns to keep (include country if available)
        keep_cols = [project_col, indicator_col, org_indicator_col, female_col, male_col]
        if country_col in df.columns:
            keep_cols.insert(1, country_col)

        gender_df = df[keep_cols].copy()

        gender_df = gender_df.merge(
            org_df[["org_indicator_id", "name"]],
            left_on=org_indicator_col,
            right_on="org_indicator_id",
            how="left",
        )

        gender_df = gender_df.melt(
            id_vars=[c for c in gender_df.columns if c not in [female_col, male_col]],
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
    org_gender_agg = gender_df.groupby(
        [org_indicator_col, "name", "Gender"], as_index=False
    )["Gender_Value"].sum()

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

    # ----------------- Gender disaggregation by country & indicator ----------------- #
    if country_col in gender_df.columns:
        st.markdown("### 🔹 Gender disaggregation by indicator for selected countries")

        gender_country_agg = gender_df.groupby(
            [country_col, "name", "Gender"], as_index=False
        )["Gender_Value"].sum()

        # Indicator selection
        ind_opts2 = sorted(gender_country_agg["name"].dropna().unique())
        selected_inds2 = st.multiselect(
            "Select indicators for gender-by-country view",
            options=ind_opts2,
            default=ind_opts2[: min(3, len(ind_opts2))],
            key="gender_country_indicator_select",
        )

        filt_gender_country = gender_country_agg[
            gender_country_agg["name"].isin(selected_inds2)
        ]

        if not filt_gender_country.empty:
            fig_gender_country = px.bar(
                filt_gender_country,
                x="name",
                y="Gender_Value",
                color="Gender",
                facet_col=country_col,
                facet_col_wrap=3,
                title="Gender breakdown by indicator and country",
            )
            fig_gender_country.update_layout(
                xaxis_title="Indicator",
                yaxis_title="Total",
            )
            st.plotly_chart(fig_gender_country, use_container_width=True)
        else:
            st.info("No gender data for the selected indicators/countries.")

    # project-level by gender (kept for completeness)
    if project_col in gender_df.columns:
        proj_gender_agg = gender_df.groupby(
            [project_col, "name", "Gender"], as_index=False
        )["Gender_Value"].sum()

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
