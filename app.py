import streamlit as st
import pandas as pd

from sqlalchemy import text
from config.config import get_engine
from sections.role_info import role_info_section
from sections.benchmarking import benchmarking_section
from sections.result_display import display_result
from handlers.generate_action import run_generate_action

# Page Config
st.set_page_config(page_title="Talent Match Intelligence", layout="wide")

# Header Section
st.title("AI Talent Match Dashboard")
st.write("Parameterize role requirements and benchmark employees to recompute talent match scoring.")

# Database Engine
engine = get_engine()

# Load Employee Data
@st.cache_data
def load_employees():
    query = "SELECT employee_id, fullname, position, grade FROM employees_performers"
    df = pd.read_sql(query, engine)
    df["label"] = df["employee_id"] + " - " + df["fullname"]
    return df

df_emp = load_employees()

# Section Role Info
role_name, role_purpose, job_level = role_info_section()

# Section Benchmarking
selected_benchmarks, benchmark_ids = benchmarking_section(df_emp)

# Submit Action
if st.button("Generate Job Description & Match Score"):
    df_result = run_generate_action(engine, benchmark_ids, role_name)
    st.session_state["df_result"] = df_result
    display_result(df_result)
elif "df_result" in st.session_state:
    display_result(st.session_state["df_result"])
