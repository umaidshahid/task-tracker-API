# Task Tracker API — FastAPI (Dockerized)

A polished starter backend project implementing a Task/Issue Tracker API using FastAPI, PostgreSQL, Alembic, JWT auth, Celery (stub), and pytest. Designed to be production-friendly and easy to clone & run with Docker Compose.

---

## Tech stack
- FastAPI  
- Python 3.11+  
- PostgreSQL  
- SQLAlchemy  
- Alembic (migrations)  
- Pydantic  
- JWT (PyJWT)  
- Celery + Redis (background jobs stub)  
- Docker & Docker Compose  
- pytest (testing)  

---

## Features (MVP)
- User registration and JWT login  
- Task CRUD (title, description, assignee, status)  
- Task statuses: `open`, `in_progress`, `done`  
- Background task: send "assignment" notification (Celery stub)  
- Alembic migrations  
- Basic unit/integration tests with pytest  

---

## Quick start (Docker Compose)

1. Copy `.env.example` to `.env` and edit values (especially `POSTGRES_PASSWORD`, `SECRET_KEY`).  

2. Build & run:

```bash
docker-compose up --build
