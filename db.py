from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from schema import *
from constant import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    json_data = Column(JSON, nullable=False)

Base.metadata.create_all(bind=engine)

def save_resume(data: ResumeData):
    session = SessionLocal()
    resume = Resume(
        candidate_name=data.candidate_name,
        email=data.contact_details.email if data.contact_details else None,
        phone=data.contact_details.phone if data.contact_details else None,
        json_data=data.model_dump()
    )
    session.add(resume)
    session.commit()
    session.refresh(resume)
    return resume


