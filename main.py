from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from utils import *
from db import save_resume
import re
import aiofiles

app = FastAPI(title="AI Resume Parser",
              version="1.0",
              description="""
              AI Resume Parser
              
              Git Repo: https://github.com/Raghven10/resume-parser.git
              
              """)

@app.post("/parse-resume/")
async def parse_resume(file: UploadFile = File(...)):
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only .pdf and .docx files are supported.")

    try:
        # Save temp file
        temp_path = f"/tmp/{file.filename}"
        async with aiofiles.open(temp_path, "wb") as f:
            content = await file.read()
            await f.write(content)

        # Extract raw text
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(temp_path)
        else:
            text = extract_text_from_docx(temp_path)

        # AI Extraction + Validation
        details = await extract_with_ai(text)

        # Save to DB
        saved = save_resume(details)

        return JSONResponse(content=details.model_dump())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing resume: {str(e)}")