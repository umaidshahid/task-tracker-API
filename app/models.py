from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import enum


Base = declarative_base()


class TaskStatus(str, enum.Enum):
open = "open"
in_progress = "in_progress"
done = "done"


class User(Base):
__tablename__ = "users"
id = Column(Integer, primary_key=True, index=True)
username = Column(String, unique=True, index=True, nullable=False)
hashed_password = Column(String, nullable=False)
tasks = relationship("Task", back_populates="assignee")


class Task(Base):
__tablename__ = "tasks"
id = Column(Integer, primary_key=True, index=True)
title = Column(String, nullable=False)
description = Column(Text, nullable=True)
status = Column(Enum(TaskStatus), default=TaskStatus.open)
assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
assignee = relationship("User", back_populates="tasks")