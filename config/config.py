import os
import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load Environment from .env
load_dotenv()

# Get Environment & Create Connection
@st.cache_resource
def get_engine():
    DB_USER = os.getenv("USERNAME_CREDENTIALS")
    DB_PASS = os.getenv("PASSWORD_CREDENTIALS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    return engine

# Export variable
DATABASE_URL = f"postgresql://{os.getenv('USERNAME_CREDENTIALS')}:{os.getenv('PASSWORD_CREDENTIALS')}@" \
               f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"