import streamlit as st

# Display Job Details
def display_job_details(job_data: dict):
    st.markdown("#### Job Details")
    st.caption("All fields below are required. You may edit or remove items as needed.")

    categories = [
        "Key Responsibilities",
        "Work Inputs",
        "Work Outputs",
        "Qualifications",
        "Competencies",
    ]

    for cat in categories:
        st.markdown(f"##### {cat}")
        items = job_data.get(cat, [])
        key_prefix = cat.replace(" ", "_").lower()

        if f"{key_prefix}_items" not in st.session_state:
            st.session_state[f"{key_prefix}_items"] = items

        new_item = st.text_input(f"Add new item to {cat}", key=f"{key_prefix}_input")
        add_col, _, _ = st.columns([0.2, 0.6, 0.2])
        if add_col.button("➕ Add", key=f"{key_prefix}_add"):
            if new_item.strip():
                st.session_state[f"{key_prefix}_items"].append(new_item.strip())
                st.success(f"Added to {cat}: {new_item}")

        for i, val in enumerate(st.session_state[f"{key_prefix}_items"]):
            c1, c2 = st.columns([0.9, 0.1])
            c1.markdown(f"- {val}")
            if c2.button("❌", key=f"{key_prefix}_del_{i}"):
                st.session_state[f"{key_prefix}_items"].pop(i)
                st.rerun()

        st.markdown("---")