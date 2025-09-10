from pydantic import BaseModel
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
open = "open"
in_progress = "in_progress"
done = "done"


class UserCreate(BaseModel):
username: str
password: str


class UserOut(BaseModel):
id: int
username: str
class Config:
orm_mode = True


class TaskBase(BaseModel):
title: str
description: Optional[str] = None


class TaskCreate(TaskBase):
assignee_id: Optional[int] = None


class TaskOut(TaskBase):
id: int
status: TaskStatus
assignee: Optional[UserOut] = None
class Config:
orm_mode = True