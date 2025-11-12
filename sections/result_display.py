import streamlit as st
import pandas as pd
import requests
import os
import json

from .result_display_sections.job_profile_api import generate_job_profile
from .result_display_sections.job_details import display_job_details

# Main Display Function
def display_result(df_result: pd.DataFrame):
    st.markdown("---")

    st.markdown("### Ranked Talent Match Result")
    st.dataframe(df_result, width="stretch")

    st.markdown("---")
    st.markdown("### 3. AI-Generated Job Profile")

    # === Tombol langsung trigger API ===
    if st.button("Generate AI Job Profile", key="generate_ai_job"):
        with st.spinner("Generating job profile using OpenRouter..."):
            ai_output = generate_job_profile(df_result)

            if not ai_output:
                st.error("Failed to generate job profile.")
                return

            st.success("Job profile generated successfully!")
            display_job_details(ai_output)
