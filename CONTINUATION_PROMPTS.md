# Continuation Prompts for AI Assistance

This file contains prompts to help another AI assistant pick up where we left off on the Oola project.

## Quick Context Prompt

```
I'm working on Oola, an AI homeschool platform for grades 1-12. It's a React + Electron frontend with Python FastAPI backend. The MVP is complete with:
- Teacher dashboard with classroom management
- Multiple LLM support (GPT/Claude/Local models via dropdown)
- Student profiles with learning styles
- AI chat interface and lesson generation
- SQLite database with offline-first architecture
- Three tiers: Individual, Family, Classroom

Read @DOCUMENTATION.md for full details. The project structure is in oola/ folder.

I need help with: [YOUR SPECIFIC TASK]
```

## Feature Development Prompts

### 1. Add Authentication System
```
I need to add JWT authentication to Oola. Currently there's no login system. Requirements:
- JWT token-based auth
- Login/logout flow
- Protected routes in React
- FastAPI dependencies for auth
- Session management
- Password reset flow

The backend already has password hashing (passlib). Teachers table exists with email/hashed_password. Update @backend/main.py and create new auth routes.
```

### 2. Implement Daily Learning Summaries
```
Add a feature where Oola generates daily learning summaries for parents. Requirements:
- Summarize all learning sessions from the day
- Include subjects covered, time spent, key concepts
- Highlight areas of strength and struggle
- Suggest tomorrow's focus areas
- Store summaries in database
- Display in parent dashboard

Use the existing learning_sessions table and add a new summary generation endpoint using the LLM service.
```

### 3. Build Weekly Assessment System
```
Create a weekly assessment feature to track student progress. Requirements:
- Generate quiz questions based on week's lessons
- Multiple choice and short answer formats
- Auto-grade with LLM assistance
- Track scores over time
- Show progress charts
- Identify knowledge gaps

Add new assessments table and integrate with existing learner profiles.
```

### 4. Add State Curriculum Database
```
Build a curriculum mapping system for US state requirements. Requirements:
- Database of learning standards by state and grade
- Map lessons to specific standards
- Track curriculum coverage
- Generate compliance reports
- Support all 50 states
- Allow custom curriculum addition

Create new curriculum tables and integrate with lesson generation in llm_service.py.
```

### 5. Implement Offline Sync
```
Add offline sync capability between desktop app and cloud. Requirements:
- Detect online/offline status
- Queue changes when offline
- Sync when connection restored
- Conflict resolution
- Progress indicator
- Background sync

Use SQLite for local storage and PostgreSQL for cloud. Add sync service to backend.
```

### 6. Create Parent Oversight Dashboard
```
Build a comprehensive parent dashboard with oversight tools. Requirements:
- View all AI conversations (chat history)
- Daily activity summaries per child
- Time spent learning by subject
- Progress charts and analytics
- Set learning goals
- Approve/block content
- Safety controls

Add new analytics endpoints and create ParentDashboard.jsx component.
```

### 7. Add Special Needs Adaptations
```
Implement UI and content adaptations for special needs learners. Requirements:
- Dyslexia-friendly fonts and spacing
- Text-to-speech integration
- Adjustable reading levels
- Visual aids and icons
- Sensory-friendly color schemes
- Customizable interface
- IEP goal tracking

Update learner profiles and create adaptive UI components.
```

### 8. Build Co-hort Group Learning
```
Add group learning features for multiple students. Requirements:
- Create learning groups within classrooms
- Group chat with Oola
- Collaborative lessons
- Peer discussion prompts
- Group projects
- Live sessions (optional)
- Asynchronous collaboration

Add groups table and update chat interface for multi-user.
```

### 9. Implement Content Safety Filters
```
Add safety guardrails for child-AI interactions. Requirements:
- Content filtering (inappropriate topics)
- Age-appropriate language
- Block harmful instructions
- Parent-configurable sensitivity
- Log flagged interactions
- Emergency stop button
- COPPA compliance features

Update llm_service.py with safety checks and add moderation layer.
```

### 10. Create Curriculum Content Library
```
Build a curated content library instead of pure AI generation. Requirements:
- Pre-written lessons by subject/grade
- Worksheets and activities
- Video resources
- Interactive exercises
- Teacher-created content
- Community contributions
- Search and filter

Create content management system with new tables and admin interface.
```

## Bug Fix Prompts

### Fix Missing Features
```
The following features are partially implemented but not working:
1. LLM provider switching doesn't persist on page refresh
2. Learning profile updates don't reflect in chat context
3. Session history doesn't display properly
4. Classroom state selection has no effect

Debug and fix these issues in @frontend/src/store/useStore.js and @backend/main.py.
```

### Database Migration
```
I need to migrate from SQLite to PostgreSQL for production. Requirements:
- Update database.py connection
- Create migration scripts
- Preserve existing data
- Add connection pooling
- Handle concurrent users
- Update .env configuration

Ensure backward compatibility with SQLite for local development.
```

## Testing Prompts

### Add Backend Tests
```
Create pytest tests for the Oola backend. Cover:
- All API endpoints
- Database models
- LLM service (with mocks)
- Authentication (when added)
- Error handling
- Edge cases

Create tests/ folder with test_main.py, test_models.py, test_llm_service.py.
```

### Add Frontend Tests
```
Create Vitest tests for React components. Cover:
- All page components
- Form submissions
- API calls (mocked)
- State management
- User interactions
- Routing

Use React Testing Library. Create __tests__/ folders in components/ and pages/.
```

## Deployment Prompts

### Deploy to Production
```
Help me deploy Oola to production. Requirements:
- Backend: Deploy FastAPI to AWS/Heroku/Railway
- Frontend: Deploy React to Vercel/Netlify
- Database: Set up PostgreSQL (AWS RDS/Supabase)
- Environment variables configuration
- HTTPS/SSL setup
- Domain configuration
- CI/CD pipeline

Provide step-by-step deployment guide.
```

### Build Desktop Installer
```
Create production-ready desktop installers. Requirements:
- Windows .exe installer
- macOS .dmg installer
- Linux .AppImage
- Auto-update functionality
- Code signing
- Installer customization

Update electron-builder config in package.json and create build scripts.
```

## Optimization Prompts

### Reduce LLM Costs
```
Optimize LLM usage to reduce API costs. Strategies:
- Cache common responses
- Use cheaper models for simple tasks
- Implement prompt compression
- Batch requests
- Add response streaming
- Local model fallback

Update llm_service.py with cost optimization strategies.
```

### Improve Performance
```
Optimize Oola for better performance. Focus on:
- Lazy loading components
- Database query optimization
- API response caching
- Bundle size reduction
- Image optimization
- Code splitting

Profile the app and implement performance improvements.
```

## Documentation Prompts

### Create User Guide
```
Write a comprehensive user guide for Oola. Include:
- Getting started tutorial
- Creating classrooms and adding students
- Using the AI chat feature
- Generating lessons
- Understanding learning profiles
- Selecting LLM providers
- Troubleshooting common issues
- FAQ section

Create USER_GUIDE.md with screenshots (describe where they should go).
```

### API Documentation
```
Generate OpenAPI/Swagger documentation for the Oola API. Include:
- All endpoints with descriptions
- Request/response schemas
- Authentication requirements
- Example requests
- Error codes
- Rate limits

Add Swagger UI to FastAPI and create API_DOCS.md.
```

## Architecture Prompts

### Refactor for Scalability
```
Refactor Oola architecture for scalability. Considerations:
- Microservices vs monolith
- Message queue for async tasks
- Caching layer (Redis)
- Load balancing
- Database sharding
- CDN for static assets
- Monitoring and logging

Propose architecture changes and implementation plan.
```

### Add Mobile App
```
Create a React Native mobile app for Oola. Requirements:
- iOS and Android support
- Share code with web app
- Offline-first architecture
- Push notifications
- Native features (camera, voice)
- Responsive design

Set up React Native project and port core features.
```

## Quick Reference

**Project Location**: `oola/`
**Backend Port**: 8000
**Frontend Port**: 3000
**Database**: SQLite (oola.db)
**Main Files**:
- Backend: `backend/main.py`, `backend/llm_service.py`
- Frontend: `frontend/src/App.jsx`, `frontend/src/store/useStore.js`
- Docs: `DOCUMENTATION.md`, `README.md`

**Key Commands**:
```bash
# Backend
cd backend && python -m uvicorn main:app --reload

# Frontend
cd frontend && npm run dev

# Desktop
cd frontend && npm run electron:dev
```

## Tips for AI Assistants

1. **Always read DOCUMENTATION.md first** - It has complete context
2. **Check existing code patterns** - Follow established conventions
3. **Test with multiple LLM providers** - Don't assume OpenAI only
4. **Consider costs** - API calls add up quickly
5. **Prioritize child safety** - This is an education platform for kids
6. **Keep it minimal** - Don't over-engineer the MVP
7. **Update docs** - Add your changes to DOCUMENTATION.md
8. **Think offline-first** - Desktop app needs to work without internet
9. **Parent control** - Parents must have oversight of all AI interactions
10. **State compliance** - Education standards vary by state

## Common Issues & Solutions

**Issue**: LLM API key not working
**Solution**: Check .env file, ensure OPENAI_API_KEY or ANTHROPIC_API_KEY is set

**Issue**: Database not found
**Solution**: Run backend once to create oola.db via SQLAlchemy

**Issue**: Frontend can't connect to backend
**Solution**: Ensure backend is running on port 8000, check CORS settings

**Issue**: Electron app won't start
**Solution**: Run `npm install` in frontend/, check electron.js paths

**Issue**: Local LLM not working
**Solution**: Install Ollama and pull models: `ollama pull llama2`

---

Use these prompts to continue development efficiently. Good luck! 🚀
