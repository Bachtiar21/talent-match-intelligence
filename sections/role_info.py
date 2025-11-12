import streamlit as st

def role_info_section():
    st.markdown("### 1. Role Information")

    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            role_name = st.text_input("Role Name", placeholder="Ex. Marketing Manager")
            role_purpose = st.text_area(
                "Role Purpose",
                placeholder="1–2 sentences to describe expected role outcome",
                height=80
            )

        with col2:
            job_level = st.selectbox(
                "Job Level",
                ["Junior", "Middle", "Senior"],
                index=1
            )

    return role_name, role_purpose, job_level
