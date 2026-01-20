# Oola - AI Homeschool Platform Documentation

## Project Overview

Oola is a personalized AI-powered education platform for grades 1-12 that enables parents/teachers to manage homeschool classrooms with AI-assisted learning. The platform supports multiple LLM providers (both API-based and local models) and provides personalized learning experiences tailored to each student's learning style, strengths, and needs.

## Core Concept

**Oola** is an AI teacher that:
- Hosts homeschool co-horts (classrooms)
- Provides curriculum based on grade level and state requirements
- Adapts to individual learning styles and special needs
- Uses real-world analogies and practical scenarios
- Tracks progress through weekly assessments
- Generates daily learning summaries for parents

## Architecture

### Tech Stack
- **Frontend**: React 18 + Vite + React Router
- **Desktop App**: Electron (for .exe distribution)
- **Backend**: Python FastAPI
- **Database**: SQLite (offline-first) with PostgreSQL support for cloud
- **LLM Integration**: LangChain with multiple providers
- **State Management**: Zustand

### Project Structure
```
oola/
├── backend/
│   ├── main.py              # FastAPI application with all routes
│   ├── models.py            # SQLAlchemy database models
│   ├── schemas.py           # Pydantic validation schemas
│   ├── database.py          # Database configuration
│   ├── llm_service.py       # Multi-provider LLM service
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── LLMSelector.jsx          # Dropdown for AI model selection
│   │   │   ├── ChatInterface.jsx        # Real-time chat with Oola
│   │   │   ├── LessonGenerator.jsx      # Generate personalized lessons
│   │   │   ├── ClassroomCard.jsx        # Classroom display card
│   │   │   ├── LearnerCard.jsx          # Student display card
│   │   │   ├── CreateClassroomModal.jsx # Modal to create classrooms
│   │   │   └── AddLearnerModal.jsx      # Modal to add students
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx            # Main teacher dashboard
│   │   │   ├── ClassroomView.jsx        # Classroom management page
│   │   │   └── LearnerView.jsx          # Student learning interface
│   │   ├── store/
│   │   │   └── useStore.js              # Zustand global state
│   │   ├── App.jsx                      # Main app with routing
│   │   ├── main.jsx                     # React entry point
│   │   ├── App.css                      # Main styles
│   │   └── index.css                    # Base styles
│   ├── electron.js          # Electron main process
│   ├── package.json         # Node dependencies & scripts
│   ├── vite.config.js       # Vite configuration
│   └── index.html           # HTML entry point
├── README.md                # Project overview
└── .gitignore              # Git ignore rules
```

## Key Features Implemented

### 1. User Roles & Management
- **Teacher/Parent Account**: Single role that manages classrooms
- **Classroom System**: Parents can create multiple classrooms (called "classrooms")
- **Multi-Student Support**: Each classroom can have multiple learners
- **Three Tiers**:
  - Individual: Single learner
  - Family: Multiple children in one household
  - Classroom: Full classroom management

### 2. LLM Provider Support
**API-Based Models:**
- GPT-3.5 Turbo (cheap, fast)
- GPT-4 (expensive, high quality)
- Claude 3 Sonnet (Anthropic)

**Local Models (via Ollama):**
- Llama 2
- Mistral
- Phi

**Auto Mode**: Automatically selects cheapest available option (defaults to GPT-3.5)

### 3. Learner Profiles
Each student has:
- Name, grade (1-12)
- Learning style (visual, auditory, kinesthetic, reading/writing)
- Learning profile (strengths, weaknesses, preferences)
- Special needs accommodations
- State curriculum requirements

### 4. AI Features
- **Chat Interface**: Real-time conversation with Oola
- **Lesson Generation**: Create personalized lessons by subject and grade
- **Context-Aware**: Oola adapts to student's learning style and profile
- **Subject Support**: Math, English, Science, History, Geography, Art, Music

### 5. Database Schema

**Teachers Table:**
- id, email, hashed_password, name, created_at

**Classrooms Table:**
- id, name, teacher_id, tier (enum), llm_provider (enum), state, created_at

**Learners Table:**
- id, name, grade, classroom_id, learning_profile (JSON), special_needs (JSON), created_at

**Learning_Sessions Table:**
- id, learner_id, subject, content (JSON), summary, duration_minutes, date

## API Endpoints

### Teacher/Parent Routes
- `POST /teachers` - Create teacher account
- `GET /teachers/{teacher_id}` - Get teacher details

### Classroom Routes
- `POST /teachers/{teacher_id}/classrooms` - Create classroom
- `GET /teachers/{teacher_id}/classrooms` - List all classrooms
- `GET /classrooms/{classroom_id}` - Get classroom details
- `PATCH /classrooms/{classroom_id}/llm` - Update LLM provider

### Learner Routes
- `POST /classrooms/{classroom_id}/learners` - Add student
- `GET /classrooms/{classroom_id}/learners` - List students
- `GET /learners/{learner_id}` - Get student details
- `PATCH /learners/{learner_id}/profile` - Update learning profile

### Learning Session Routes
- `POST /learners/{learner_id}/sessions` - Create learning session
- `GET /learners/{learner_id}/sessions` - Get session history

### AI Routes
- `POST /ai/lesson` - Generate personalized lesson
- `POST /ai/chat` - Chat with Oola

## Environment Setup

### Backend Environment Variables (.env)
```
DATABASE_URL=sqlite:///./oola.db
SECRET_KEY=your-secret-key-change-in-production
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
OLLAMA_BASE_URL=http://localhost:11434
```

### Frontend Environment Variables
```
VITE_API_URL=http://localhost:8000
```

## Installation & Running

### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python -m uvicorn main:app --reload
```
Backend runs on: http://localhost:8000

### Frontend (Web)
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on: http://localhost:3000

### Desktop App (.exe)
```bash
cd frontend
npm run electron:dev
```

### Build Desktop App
```bash
cd frontend
npm run electron:build
```
Output in `frontend/release/`

## Current State & What Works

✅ **Fully Functional:**
- Teacher account creation
- Classroom creation with tier selection
- Student management (add, view, list)
- LLM provider selection (dropdown)
- AI chat interface
- Lesson generation
- Learning profile storage
- Database persistence (SQLite)
- React routing between pages
- Electron desktop wrapper

⚠️ **Partially Implemented:**
- Authentication (password hashing exists, but no JWT/sessions)
- State curriculum mapping (state field exists, but no curriculum data)
- Progress tracking (sessions table exists, but no analytics)
- Special needs (field exists, but no adaptive UI)

❌ **Not Yet Implemented:**
- User login/logout flow
- Daily learning summaries for parents
- Weekly assessments
- Co-hort/group learning features
- Offline sync mechanism
- Content filtering/safety guardrails
- COPPA compliance features
- University prep tracks
- Advanced course acceleration

## Design Decisions

1. **Offline-First**: SQLite for local storage, can sync to PostgreSQL cloud
2. **Minimal MVP**: Focus on core features, avoid over-engineering
3. **Free Tier Friendly**: Default to cheapest LLM options
4. **Parent Control**: Parents have full oversight of AI interactions
5. **Flexible LLM**: Support both API and local models for cost/privacy options
6. **No Authentication Yet**: Simplified for MVP, add JWT later
7. **JSON Profiles**: Flexible learning_profile and special_needs as JSON for easy extension

## Known Limitations

1. No authentication system (anyone can access any data)
2. No real-time sync between web and desktop app
3. No curriculum content database (Oola generates from scratch)
4. No assessment/testing system
5. No parent dashboard analytics
6. No content safety filters
7. No session persistence in chat (messages lost on refresh)
8. No file uploads (worksheets, assignments)
9. No calendar/scheduling system
10. No payment/subscription system

## Dependencies

### Backend (Python)
- fastapi==0.104.1
- uvicorn==0.24.0
- sqlalchemy==2.0.23
- psycopg2-binary==2.9.9 (for PostgreSQL)
- pydantic==2.5.0
- passlib[bcrypt]==1.7.4
- langchain==0.1.0
- langchain-openai==0.0.2
- langchain-anthropic==0.0.1
- langchain-community==0.0.13
- ollama==0.1.6
- python-dotenv==1.0.0

### Frontend (Node.js)
- react==18.2.0
- react-dom==18.2.0
- react-router-dom==6.20.0
- axios==1.6.2
- zustand==4.4.7
- vite==5.0.0
- electron==28.0.0
- electron-builder==24.9.1

## Security Considerations

⚠️ **Current Security Issues (MVP only):**
- No authentication/authorization
- CORS allows all origins
- No rate limiting
- No input sanitization
- API keys in .env (not encrypted)
- No HTTPS enforcement
- No COPPA compliance

🔒 **Must Add Before Production:**
- JWT authentication
- Role-based access control
- Input validation and sanitization
- Rate limiting
- HTTPS/TLS
- API key encryption
- Content filtering for children
- COPPA compliance (parental consent, data privacy)
- Session management
- CSRF protection

## Future Enhancements Roadmap

### Phase 1 (MVP Complete) ✅
- Basic dashboard
- LLM integration
- Student profiles
- Chat and lesson generation

### Phase 2 (Core Features)
- [ ] Authentication (JWT)
- [ ] Daily learning summaries
- [ ] Weekly assessments
- [ ] Progress tracking dashboard
- [ ] State curriculum database
- [ ] Learning style adaptation engine

### Phase 3 (Advanced Features)
- [ ] Co-hort group learning
- [ ] Live sessions
- [ ] Advanced courses
- [ ] University prep tracks
- [ ] Special needs UI adaptations
- [ ] Parent oversight tools
- [ ] Content safety filters

### Phase 4 (Production Ready)
- [ ] Payment system (Stripe)
- [ ] Cloud sync (PostgreSQL)
- [ ] Mobile app (React Native)
- [ ] Analytics dashboard
- [ ] Curriculum marketplace
- [ ] Teacher certification
- [ ] COPPA compliance
- [ ] Multi-language support

## Testing

Currently no tests implemented. Recommended:
- Backend: pytest for API tests
- Frontend: Vitest + React Testing Library
- E2E: Playwright or Cypress
- LLM: Mock responses for consistent testing

## Performance Considerations

- **LLM Costs**: API calls can be expensive at scale
- **Context Windows**: Long conversations may exceed token limits
- **Database**: SQLite works for single user, needs PostgreSQL for multi-user
- **Electron Size**: Desktop app will be ~200MB
- **Offline Storage**: Need to manage local storage limits

## Contributing Guidelines

When continuing this project:
1. Keep code minimal and focused
2. Follow existing patterns (Zustand for state, FastAPI routes)
3. Add environment variables to .env.example
4. Update this documentation
5. Test with multiple LLM providers
6. Consider cost implications of API calls
7. Prioritize child safety features

## License

Not yet specified - decide before open sourcing

## Contact & Support

Project created as MVP prototype. No official support yet.

---

**Last Updated**: Initial MVP completion
**Version**: 0.1.0
**Status**: Prototype/MVP
