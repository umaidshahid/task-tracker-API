from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# User helpers
async def create_user(db: AsyncSession, username: str, password: str):
hashed = pwd_context.hash(password)
user = models.User(username=username, hashed_password=hashed)
db.add(user)
await db.commit()
await db.refresh(user)
return user


async def get_user_by_username(db: AsyncSession, username: str):
q = select(models.User).where(models.User.username == username)
res = await db.execute(q)
return res.scalars().first()


# Tasks
async def create_task(db: AsyncSession, task_in: schemas.TaskCreate):
task = models.Task(title=task_in.title, description=task_in.description, assignee_id=task_in.assignee_id)
db.add(task)
await db.commit()
await db.refresh(task)
return task


async def list_tasks(db: AsyncSession):
q = select(models.Task)
res = await db.execute(q)
return res.scalars().all()


async def get_task(db: AsyncSession, task_id: int):
q = select(models.Task).where(models.Task.id == task_id)
res = await db.execute(q)
return res.scalars().first()


async def update_task(db: AsyncSession, task: models.Task, data: dict):
for k, v in data.items():
setattr(task, k, v)
db.add(task)
await db.commit()
await db.refresh(task)
return task


async def delete_task(db: AsyncSession, task: models.Task):
await db.delete(task)
await db.commit()
return True