import sys
import time
import json
import requests
import streamlit as st
import pandas as pd

from .parser import parse_ai_output

# Generate Job Profile
def generate_job_profile(df_result: pd.DataFrame):
    import sys
    import time
    if "api" in st.secrets:
        api_key = st.secrets["api"]["OPENROUTER_API_KEY"]
    else:
        api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        st.error("OPENROUTER_API_KEY tidak ditemukan di .env")
        return {}
    top3 = df_result.head(3).to_dict(orient="records")

    prompt = f"""
    You are an HR data analyst AI.
    Based on these top performing employees and their match rates:
    {json.dumps(top3, indent=2)}

    Generate a structured job profile with:
    - Key Responsibilities (5–7 concise bullet points)
    - Work Inputs (3–5 bullet points)
    - Work Outputs (3–5 bullet points)
    - Qualifications (3–5 bullet points)
    - Competencies (5–7 bullet points)

    Write in professional English, no intro text.
    """

    try:
        print("🚀 Sending request to OpenRouter...", file=sys.stderr)
        start_time = time.time()

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://talent-match-intelligence.streamlit.app",
                "X-Title": "Talent Match Intelligence",
            },
            json={
                "model": "kwaipilot/kat-coder-pro:free",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
            },
            timeout=90,
        )

        duration = round(time.time() - start_time, 2)

        if response.status_code != 200:
            st.error(f"Response error: {response.status_code}")
            return {}

        result = response.json()
        if "choices" not in result or not result["choices"]:
            st.error(f"Response tidak valid: {result}")
            return {}

        text = result["choices"][0]["message"]["content"]
        return parse_ai_output(text)

    except Exception as e:
        st.error(f"Error calling OpenRouter API : {e}")
        print("Exception detail:", e, file=sys.stderr)
        return {}