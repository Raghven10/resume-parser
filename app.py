import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/parse-resume"  # Adjust if running on different host/port

st.set_page_config(page_title="AI Resume Parser", layout="wide")


# --- Header ---
st.markdown(
    """
    <div style="text-align:center; padding: 20px; background: linear-gradient(90deg, #6a11cb, #2575fc); color: white; border-radius: 12px; margin-bottom:10px;">
        <h1>📄 AI Resume Parser</h1>
        <p>A FastAPI-based service that extracts structured candidate information (name, contact details, education, work experience, skills, salary expectations, etc.) from resumes in PDF or DOCX format.
        It leverages OpenAI / Groq LLMs for semantic extraction, Pydantic for schema validation, and stores parsed data in a Postgres database for further usage.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    files = {"file": uploaded_file}
    with st.spinner("Parsing resume... ⏳"):
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()

        # Handle missing keys gracefully
        candidate = result.get("resume_data", {})
        name = candidate.get("name", "Information not available")
        email = candidate.get("email", "Information not available")
        phone = candidate.get("phone", "Information not available")
        skills = ", ".join(candidate.get("skills", [])) if candidate.get("skills") else "Information not available"
        education = candidate.get("education", "Information not available")
        experience = candidate.get("experience", "Information not available")

        # Two column layout
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("👤 Candidate Info")

            st.write(f"**Name:** {result.get('candidate_name')}")
            st.write(f"**Address:** {result.get('address')}")

            if result.get("contact_details"):
                st.write(f"**Phone:** {result['contact_details'].get('phone')}")
                st.write(f"**Email:** {result['contact_details'].get('email')}")

            st.markdown("---")

            st.subheader("🎓 Education")
            for edu in result.get("education", []):
                st.write(f"- {edu.get('degree')} at {edu.get('institution')} ({edu.get('year')})")

            st.markdown("---")

            st.subheader("💼 Work Experience")
            if result.get("work_experiences"):
                for exp in result.get("work_experiences", []):
                    st.write(f"- {exp.get('role')} at {exp.get('company')} ({exp.get('duration')})")
            else:
                st.write("No work experience")

            st.markdown("---")

            st.subheader("📂 Projects")
            if result.get("projects"):
                for proj in result.get("projects", []):
                    st.write(
                        f"- **{proj.get('title')}**: {proj.get('description')} ({', '.join(proj.get('technologies', []))})")
            else:
                st.write("Not Mentioned")

            st.markdown("---")

            st.subheader("🛠️ Skills")
            st.write(", ".join(result.get("key_skillsets", [])))

            st.markdown("---")

            st.subheader("💰 Salary")
            st.write(f"- Last Salary: {result.get('last_salary')}")
            st.write(f"- Expected Salary: {result.get('expected_salary')}")

        with col2:
            st.subheader("📌 Extracted JSON Data")
            st.code(json.dumps(result, indent=4), language="json")



    else:
        st.error(f"Error parsing resume: {response.text}")

# ---------- Footer with Developer Info ----------
st.markdown("---")
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 30px; padding: 10px; position: relative;">
        <img src="https://avatars.githubusercontent.com/Raghven10" 
             alt="Developer Avatar" 
             style="width: 50px; height: 50px; border-radius: 50%; margin-right: 15px; border: 2px solid #7873f5;">
        <div>
            <p style="margin: 0; color: #666; font-size: 14px;">
                👨‍💻 Developed by <a href="https://github.com/Raghven10" target="_blank" style="color: #7873f5; text-decoration: none;">RK Jha</a><br>
                <span style="font-size: 12px;">PhD Researcher | AI & NLP Enthusiast</span>
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)