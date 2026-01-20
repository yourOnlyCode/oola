# Oola - AI Homeschool Platform

Personalized AI-powered education platform for grades 1-12.

## Features
- Parent/Teacher dashboard with classroom management
- Multiple LLM support (Local: Llama/Mistral/Phi, API: GPT/Claude)
- Personalized learning paths with state curriculum compliance
- Offline-first architecture with cloud sync
- Three tiers: Individual, Family, Classroom

## Tech Stack
- Frontend: React + Electron
- Backend: Python FastAPI
- Database: PostgreSQL + SQLite (offline)
- LLM: LangChain with multiple providers

## Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Desktop App
```bash
cd frontend
npm run electron:dev
```

## Project Structure
```
oola/
├── backend/          # FastAPI server
├── frontend/         # React web + Electron app
└── database/         # Schema and migrations
```
