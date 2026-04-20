
from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

class Task(BaseModel):
    id: int
    project_id: int
    title: str
    priority: int
    completed: bool = False
    due_date: Optional[date] = None
    
class Project(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    tasks: list["Task"] = []
    
