import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load Environment from .env
load_dotenv()

# Get Environment & Create Connection
@st.cache_resource
def get_engine():
    if "database" in st.secrets:
        db = st.secrets["database"]
        DB_USER = db["USERNAME_CREDENTIALS"]
        DB_PASS = db["PASSWORD_CREDENTIALS"]
        DB_HOST = db["DB_HOST"]
        DB_PORT = db["DB_PORT"]
        DB_NAME = db["DB_NAME"]
    else:
        DB_USER = os.getenv("USERNAME_CREDENTIALS")
        DB_PASS = os.getenv("PASSWORD_CREDENTIALS")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_NAME = os.getenv("DB_NAME")

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    return engine

# Export variable
if "database" in st.secrets:
    db = st.secrets["database"]
    DATABASE_URL = f"postgresql://{db['USERNAME_CREDENTIALS']}:{db['PASSWORD_CREDENTIALS']}@" \
                   f"{db['DB_HOST']}:{db['DB_PORT']}/{db['DB_NAME']}"
else:
    DATABASE_URL = f"postgresql://{os.getenv('USERNAME_CREDENTIALS')}:{os.getenv('PASSWORD_CREDENTIALS')}@" \
                   f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"