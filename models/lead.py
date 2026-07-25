from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, unique=True, index=True)
    website = Column(String)
    industry = Column(String)
    score = Column(Float)
    status = Column(String, default="new")
    research_summary = Column(Text)
    connection_note = Column(Text)
    follow_up_dm = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
