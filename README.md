# 🧠 Talent Match Intelligence

An AI-powered HR analytics dashboard built with **Streamlit** that benchmarks employee performance and generates **AI-based Job Profiles** using the OpenRouter API (LLM inference gateway).  

This project allows HR teams to:
- Upload or connect employee performance data.
- Benchmark top-performing employees.
- Automatically generate structured job descriptions with AI.

---

## 🚀 Features

- 🧾 Employee performance benchmarking  
- 🤖 AI-generated job profile creation (via OpenRouter API)  
- 📊 Dynamic data display and interaction using Streamlit  
- 💾 Modular codebase with reusable sections  
- 🔒 Secure environment variable management via `.env`  

---

## 🏗️ Project Structure

```bash
talent-match-intelligence/
├── app.py
├── requirements.txt
├── .env.example
│
├── config/
│   └── config.py
│
├── handlers/
│   └── generate_action.py
│
├── sections/
│   ├── result_display.py
│   ├── role_info.py
│   ├── benchmarking.py
│   ├── visualization.py
│   │
│   └── result_display_sections/
│       ├── job_details.py
│       ├── job_profile_api.py
│       ├── parser.py
│       └── __init__.py
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/talent-match-intelligence.git
cd talent-match-intelligence
```

### 2️⃣ Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create Environment Variables
Duplicate `.env.example` → rename to `.env`, then fill in your API keys and database connection string.

Example:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

Then open your browser at:
👉 http://localhost:8501

---

## 🧩 Deployment Options

### 🔹 Streamlit Cloud (Recommended for Demo)
1. Push this project to GitHub.
2. Visit [streamlit.io/cloud](https://share.streamlit.io)
3. Click **New App** → select your repo.
4. Set the main file path to `app.py`.
5. Add environment variables via the “Advanced Settings” panel.
6. Click **Deploy** ✅

### 🔹 Docker (for VPS / Production)
Build and run manually:
```bash
docker build -t talent-match-app .
docker run -p 8501:8501 --env-file .env talent-match-app
```

---

## 🧠 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend Logic**: Python 3.11
- **Data Layer**: SQLAlchemy (PostgreSQL)
- **AI Model**: OpenRouter API (LLM models like `mistralai/mixtral-8x7b:free`, `kwaipilot/kat-coder-pro:free`)
- **Deployment**: Streamlit Cloud / Docker

---

## 📄 Example .env File

```env
OPENROUTER_API_KEY=sk-xxxxx
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

---

## 🧑‍💻 Author

**Bachtiar Ramadhan**  
Full-stack Developer & Data Engineering Enthusiast  
📧 your-email@example.com  
🌐 [linkedin.com/in/bachtiar-ramadhan](https://linkedin.com/in/bachtiar-ramadhan)

---

## 🪪 License
This project is licensed under the **MIT License** — feel free to use, modify, and distribute with attribution.

---

> 💬 *“Empower HR analytics with data-driven insights and AI intelligence.”*
