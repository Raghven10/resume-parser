from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Education(BaseModel):
    degree: str
    institution: str
    year: Optional[str]

class WorkExperience(BaseModel):
    company: str
    role: str
    duration: Optional[str]
    responsibilities: Optional[str]

class Project(BaseModel):
    title: str
    description: Optional[str]
    technologies: Optional[List[str]]

class ContactDetails(BaseModel):
    phone: Optional[str]
    email: Optional[EmailStr]

class ResumeData(BaseModel):
    candidate_name: str
    address: Optional[str]
    contact_details: ContactDetails
    education: Optional[List[Education]]
    work_experiences: Optional[List[WorkExperience]]
    projects: Optional[List[Project]]
    key_skillsets: Optional[List[str]]
    last_salary: Optional[str]
    expected_salary: Optional[str]
