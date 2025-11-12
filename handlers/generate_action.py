import streamlit as st
import pandas as pd
from sqlalchemy import text

# Run Generate Action
def run_generate_action(engine, benchmark_ids, role_name):
    """
    Handle action untuk tombol Generate:
    - Input Validation
    - Load and running query.sql
    - Return result DataFrame
    """

    # Input Validation
    if not benchmark_ids or len(benchmark_ids) == 0:
        st.warning("Please select at least one benchmark employee.")
        st.stop()

    if not role_name:
        st.warning("Please enter a role name before generating results.")
        st.stop()

    st.success("Input received. Running match scoring ...")

    # Load Query File
    try:
        with open("query.sql") as f:
            sql_template = text(f.read())
    except FileNotFoundError:
        st.error("The ‘query.sql’ file was not found in the project directory.")
        st.stop()

    # Convert the parameter to array format postgres
    # PostgreSQL expects '{EMP1,EMP2,EMP3}' format for ANY()
    try:
        pg_array_literal = "{" + ",".join(benchmark_ids) + "}"
    except Exception:
        st.error("Failed to convert the benchmark_ids list to a PostgreSQL array.")
        st.stop()

    # Running the Query
    try:
        df_result = pd.read_sql(
            sql_template,
            engine,
            params={
                "benchmark_ids": pg_array_literal,
                "role_name": role_name,
            },
        )

        if df_result.empty:
            st.warning("The query was successfully executed, but no data was found.")
        return df_result

    except Exception as e:
        st.error(f"Failed to execute query : {e}")
        st.stop()
