


# 📄 AI Resume Parser API

## 1. Introduction

The **AI Resume Parser API** is a FastAPI-based service that extracts **structured candidate information** (name, contact details, education, work experience, skills, salary expectations, etc.) from resumes in **PDF or DOCX** format.

It leverages **OpenAI / Groq LLMs** for semantic extraction, **Pydantic** for schema validation, and stores parsed data in a **Postgres database** for further usage.

---

## 2. Features

✅ Upload **PDF/DOCX** resumes
✅ Extract structured JSON with:

* Candidate name
* Address
* Contact details (phone, email)
* Education (degree, institution, year)
* Work experience (company, role, duration)
* Projects (title, description, technologies)
* Skills
* Salary (last + expected)

✅ **LLM-powered** extraction (OpenAI/Groq)
✅ **Pydantic validation** ensures consistent JSON output
✅ Store extracted resumes in **Postgres**

---

## 3. Installation

### 🔹 Step 1: Clone the repository

```bash
git clone https://github.com/Raghven10/resume-parser.git
cd resume-parser
```

### 🔹 Step 2: Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 🔹 Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configuration

1. Copy `.env.example` → `.env` and set environment variables:

```env
OPENAI_API_KEY=your_openai_key_here
GROQ_API_KEY=your_groq_key_here
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/resumedb
```

2. Update `USE_PROVIDER` in `main.py` to choose between **openai** or **groq**.

---

## 5. Database Setup

Make sure you have **PostgreSQL** running. Then create the DB:

```bash
createdb resumedb
```

Run migrations (simple table creation):

```bash
python -c "from db import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

## 6. Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

API will be available at:
👉 `http://127.0.0.1:8000`

Interactive Swagger Docs:
👉 `http://127.0.0.1:8000/docs`

---

---

## 7. Running with Docker

### 🔹 Step 1: Build and start containers

```bash
docker-compose up --build
```

This will start:

* **resume-api** → FastAPI app on port `8000`
* **db** → Postgres database on port `5432`

### 🔹 Step 2: Access API

* API: [http://localhost:8000](http://localhost:8000)
* Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 8. Example Usage

### Upload Resume (PDF/DOCX)

```bash
curl -X POST "http://127.0.0.1:8000/parse-resume/" \
  -F "file=@resume.pdf"
```

### Example JSON Response

```json
{
  "candidate_name": "John Doe",
  "address": "123 Main Street, New York, NY",
  "contact_details": {
    "phone": "+1 9876543210",
    "email": "john.doe@example.com"
  },
  "education": [
    {"degree": "B.Sc. Computer Science", "institution": "NYU", "year": "2016"}
  ],
  "work_experiences": [
    {"company": "Google", "role": "Software Engineer", "duration": "2018-2021"}
  ],
  "projects": [
    {"title": "AI Chatbot", "description": "Built a customer service chatbot", "technologies": ["Python", "TensorFlow"]}
  ],
  "key_skillsets": ["Python", "FastAPI", "Machine Learning", "NLP"],
  "last_salary": "120000 USD",
  "expected_salary": "150000 USD"
}
```

---

## 9. Tech Stack

* **FastAPI** – API Framework
* **OpenAI/Groq API** – LLM-powered parsing
* **Pydantic** – Data validation
* **SQLAlchemy + Postgres** – Database
* **PyMuPDF / docx2txt** – Resume text extraction

---

## 10. Contributing

1. Fork the repo
2. Create a new branch (`feature/my-feature`)
3. Commit your changes
4. Push and create a PR 🚀

---

## 👨‍💻 Developer

<a href="https://github.com/Raghven10">
  <img src="https://avatars.githubusercontent.com/Raghven10" width="120px" style="border-radius:50%;" />
</a>

**[Raghvendra Kumar Jha](https://github.com/Raghven10)**  
📌 Developer & Maintainer of Resume Parser API  
💻 Passionate about NLP, FastAPI, and Generative AI  

[![GitHub followers](https://img.shields.io/github/followers/Raghven10?style=social)](https://github.com/Raghven10)  
[![GitHub stars](https://img.shields.io/github/stars/Raghven10?style=social)](https://github.com/Raghven10?tab=repositories)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/raghvendra-kumar-jha-15b64416b/)  
[![Twitter Follow](https://img.shields.io/twitter/follow/raghven11?style=social)](https://twitter.com/raghven11)
