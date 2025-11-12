import streamlit as st

def benchmarking_section(df_emp):
    st.markdown("### 2. Employee Benchmarking")

    selected_benchmarks = st.multiselect(
        "Select Employee Benchmarking (max 3)",
        df_emp["label"],
        max_selections=3
    )

    benchmark_ids = [x.split(" - ")[0] for x in selected_benchmarks]
    return selected_benchmarks, benchmark_ids
