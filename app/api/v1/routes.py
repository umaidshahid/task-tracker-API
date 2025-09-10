from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud, db
from app.core.security import create_access_token
from datetime import timedelta
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Auth endpoints
@router.post('/auth/register', response_model=schemas.UserOut)
async def register(user_in: schemas.UserCreate, session: AsyncSession = Depends(db.get_db)):
    existing = await crud.get_user_by_username(session, user_in.username)
    if existing:
        raise HTTPException(status_code=400, detail='username taken')
    user = await crud.create_user(session, user_in.username, user_in.password)
    return user

@router.post('/auth/login')
async def login(user_in: schemas.UserCreate, session: AsyncSession = Depends(db.get_db)):
    user = await crud.get_user_by_username(session, user_in.username)
    if not user or not pwd_context.verify(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail='invalid credentials')
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

# Task endpoints
@router.get('/tasks', response_model=list[schemas.TaskOut])
async def get_tasks(session: AsyncSession = Depends(db.get_db)):
    return await crud.list_tasks(session)

@router.post('/tasks', response_model=schemas.TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: schemas.TaskCreate, session: AsyncSession = Depends(db.get_db)):
    task = await crud.create_task(session, task_in)
    # Optional: trigger Celery background task here
    return task

@router.get('/tasks/{task_id}', response_model=schemas.TaskOut)
async def get_task(task_id: int, session: AsyncSession = Depends(db.get_db)):
    task = await crud.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='not found')
    return task

@router.patch('/tasks/{task_id}', response_model=schemas.TaskOut)
async def patch_task(task_id: int, data: dict, session: AsyncSession = Depends(db.get_db)):
    task = await crud.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='not found')
    updated = await crud.update_task(session, task, data)
    return updated

@router.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, session: AsyncSession = Depends(db.get_db)):
    task = await crud.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='not found')
    await crud.delete_task(session, task)
    return
