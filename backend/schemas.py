from pydantic import BaseModel, EmailStr
from typing import Optional, Dict
from datetime import datetime
from models import TierEnum, LLMProviderEnum

class TeacherCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

class TeacherResponse(BaseModel):
    id: int
    email: str
    name: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class ClassroomCreate(BaseModel):
    name: str
    tier: TierEnum = TierEnum.INDIVIDUAL
    llm_provider: LLMProviderEnum = LLMProviderEnum.AUTO
    state: str = "US"

class ClassroomResponse(BaseModel):
    id: int
    name: str
    tier: TierEnum
    llm_provider: LLMProviderEnum
    state: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class LearnerCreate(BaseModel):
    name: str
    grade: int
    learning_profile: Optional[Dict] = {}
    special_needs: Optional[Dict] = {}

class LearnerResponse(BaseModel):
    id: int
    name: str
    grade: int
    classroom_id: int
    learning_profile: Dict
    special_needs: Dict
    created_at: datetime
    
    class Config:
        from_attributes = True

class LearningSessionCreate(BaseModel):
    subject: str
    content: Dict

class LearningSessionResponse(BaseModel):
    id: int
    learner_id: int
    subject: str
    summary: Optional[str]
    duration_minutes: Optional[int]
    date: datetime
    
    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    learner_id: int
    message: str
    subject: Optional[str] = None
