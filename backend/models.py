from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base

class TierEnum(str, enum.Enum):
    INDIVIDUAL = "individual"
    FAMILY = "family"
    CLASSROOM = "classroom"

class LLMProviderEnum(str, enum.Enum):
    AUTO = "auto"
    GPT4 = "gpt-4"
    GPT35 = "gpt-3.5-turbo"
    CLAUDE = "claude-3-sonnet"
    LLAMA = "llama2"
    MISTRAL = "mistral"
    PHI = "phi"

class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    classrooms = relationship("Classroom", back_populates="teacher")

class Classroom(Base):
    __tablename__ = "classrooms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    tier = Column(Enum(TierEnum), default=TierEnum.INDIVIDUAL)
    llm_provider = Column(Enum(LLMProviderEnum), default=LLMProviderEnum.AUTO)
    state = Column(String, default="US")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    teacher = relationship("Teacher", back_populates="classrooms")
    learners = relationship("Learner", back_populates="classroom")

class Learner(Base):
    __tablename__ = "learners"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    grade = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))
    learning_profile = Column(JSON, default={})
    special_needs = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    
    classroom = relationship("Classroom", back_populates="learners")
    sessions = relationship("LearningSession", back_populates="learner")

class LearningSession(Base):
    __tablename__ = "learning_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learners.id"))
    subject = Column(String)
    content = Column(JSON)
    summary = Column(String)
    duration_minutes = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)
    
    learner = relationship("Learner", back_populates="sessions")
