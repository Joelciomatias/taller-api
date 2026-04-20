from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from backend.model import Project, Task

app = FastAPI()




@app.post("/projects")
def create_project(project: Project):
    return project

@app.get("/projects/{id}")
def read_project(id: int, q: str | None = None):
    return {"id": id, "q": q}

@app.put("/projects/{project_id}")
async def update_project(project_id: int, project: Project):
    return {"project_id": project_id, **project.model_dump()}

@app.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    return {"project_id": project_id, "message": "Project deleted successfully"}