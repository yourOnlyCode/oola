from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db
from llm_service import llm_service
from passlib.context import CryptContext

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Oola API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Teacher/Parent Routes
@app.post("/teachers", response_model=schemas.TeacherResponse)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(teacher.password)
    db_teacher = models.Teacher(
        email=teacher.email,
        hashed_password=hashed_password,
        name=teacher.name
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.get("/teachers/{teacher_id}", response_model=schemas.TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# Classroom Routes
@app.post("/teachers/{teacher_id}/classrooms", response_model=schemas.ClassroomResponse)
def create_classroom(teacher_id: int, classroom: schemas.ClassroomCreate, db: Session = Depends(get_db)):
    db_classroom = models.Classroom(**classroom.dict(), teacher_id=teacher_id)
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

@app.get("/teachers/{teacher_id}/classrooms", response_model=List[schemas.ClassroomResponse])
def get_classrooms(teacher_id: int, db: Session = Depends(get_db)):
    return db.query(models.Classroom).filter(models.Classroom.teacher_id == teacher_id).all()

@app.get("/classrooms/{classroom_id}", response_model=schemas.ClassroomResponse)
def get_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(models.Classroom).filter(models.Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom

@app.patch("/classrooms/{classroom_id}/llm")
def update_llm_provider(classroom_id: int, provider: models.LLMProviderEnum, db: Session = Depends(get_db)):
    classroom = db.query(models.Classroom).filter(models.Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    classroom.llm_provider = provider
    db.commit()
    return {"message": "LLM provider updated", "provider": provider}

# Learner Routes
@app.post("/classrooms/{classroom_id}/learners", response_model=schemas.LearnerResponse)
def create_learner(classroom_id: int, learner: schemas.LearnerCreate, db: Session = Depends(get_db)):
    db_learner = models.Learner(**learner.dict(), classroom_id=classroom_id)
    db.add(db_learner)
    db.commit()
    db.refresh(db_learner)
    return db_learner

@app.get("/classrooms/{classroom_id}/learners", response_model=List[schemas.LearnerResponse])
def get_learners(classroom_id: int, db: Session = Depends(get_db)):
    return db.query(models.Learner).filter(models.Learner.classroom_id == classroom_id).all()

@app.get("/learners/{learner_id}", response_model=schemas.LearnerResponse)
def get_learner(learner_id: int, db: Session = Depends(get_db)):
    learner = db.query(models.Learner).filter(models.Learner.id == learner_id).first()
    if not learner:
        raise HTTPException(status_code=404, detail="Learner not found")
    return learner

@app.patch("/learners/{learner_id}/profile")
def update_learner_profile(learner_id: int, profile: dict, db: Session = Depends(get_db)):
    learner = db.query(models.Learner).filter(models.Learner.id == learner_id).first()
    if not learner:
        raise HTTPException(status_code=404, detail="Learner not found")
    learner.learning_profile = {**learner.learning_profile, **profile}
    db.commit()
    return {"message": "Profile updated", "profile": learner.learning_profile}

# Learning Session Routes
@app.post("/learners/{learner_id}/sessions", response_model=schemas.LearningSessionResponse)
def create_session(learner_id: int, session: schemas.LearningSessionCreate, db: Session = Depends(get_db)):
    db_session = models.LearningSession(
        learner_id=learner_id,
        subject=session.subject,
        content=session.content
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@app.get("/learners/{learner_id}/sessions", response_model=List[schemas.LearningSessionResponse])
def get_sessions(learner_id: int, db: Session = Depends(get_db)):
    return db.query(models.LearningSession).filter(models.LearningSession.learner_id == learner_id).all()

# AI/LLM Routes
@app.post("/ai/lesson")
def generate_lesson(learner_id: int, subject: str, db: Session = Depends(get_db)):
    learner = db.query(models.Learner).filter(models.Learner.id == learner_id).first()
    if not learner:
        raise HTTPException(status_code=404, detail="Learner not found")
    
    classroom = learner.classroom
    lesson_content = llm_service.generate_lesson(
        learner.learning_profile,
        subject,
        learner.grade,
        classroom.llm_provider
    )
    
    return {"lesson": lesson_content, "subject": subject, "grade": learner.grade}

@app.post("/ai/chat")
def chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    learner = db.query(models.Learner).filter(models.Learner.id == request.learner_id).first()
    if not learner:
        raise HTTPException(status_code=404, detail="Learner not found")
    
    context = {
        "learner_name": learner.name,
        "grade": learner.grade,
        "subject": request.subject,
        "learning_style": learner.learning_profile.get("learning_style", "visual")
    }
    
    response = llm_service.chat_with_student(
        request.message,
        context,
        learner.classroom.llm_provider
    )
    
    return {"response": response}

@app.get("/")
def root():
    return {"message": "Oola API - AI Homeschool Platform"}
