# Task Tracker API — FastAPI (Dockerized)

A polished starter backend project implementing a Task/Issue Tracker API using FastAPI, PostgreSQL, Alembic, JWT auth, Celery (stub), and pytest. Designed to be production-friendly and easy to clone & run with Docker Compose.

---

## Tech stack

* FastAPI
* Python 3.11+
* PostgreSQL
* SQLAlchemy
* Alembic (migrations)
* Pydantic
* JWT (PyJWT)
* Celery + Redis (background jobs stub)
* Docker & Docker Compose
* pytest (testing)

---

## Features (MVP)

* User registration and JWT login
* Task CRUD (title, description, assignee, status)
* Task statuses: `open`, `in_progress`, `done`
* Background task: send "assignment" notification (Celery stub)
* Alembic migrations
* Basic unit/integration tests with pytest

---

## Quick start (Docker Compose)

1. Copy `.env.example` to `.env` and edit values (especially `POSTGRES_PASSWORD`, `SECRET_KEY`).
2. Build & run:

```bash
docker-compose up --build
```

3. API available at:

* `http://localhost:8000`
* Swagger docs: `http://localhost:8000/docs`

---

## Environment variables

Use `.env` (see `.env.example`):

```env
POSTGRES_USER=task_user
POSTGRES_PASSWORD=task_password
POSTGRES_DB=task_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://task_user:task_password@db:5432/task_db
SECRET_KEY=replace-this-with-a-secure-random-string
ACCESS_TOKEN_EXPIRE_MINUTES=60
REDIS_URL=redis://redis:6379/0
```

---

## Endpoints (examples)

* `POST /api/v1/auth/register` — register new user `{username, password}`
* `POST /api/v1/auth/login` — returns JWT `{access_token}`
* `GET /api/v1/tasks` — list tasks (auth)
* `POST /api/v1/tasks` — create task `{title, description, assignee_id?}` (auth)
* `GET /api/v1/tasks/{id}` — get task by id
* `PATCH /api/v1/tasks/{id}` — update task fields
* `DELETE /api/v1/tasks/{id}` — delete task

---

## Running tests

```bash
# inside container OR with your virtualenv installed
pytest -q
```

---
