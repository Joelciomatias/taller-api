from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    priority: int
    completed: bool = False
    due_date: Optional[date] = None


class Task(TaskBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

