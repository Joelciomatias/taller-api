from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import ProjectORM, get_db
from backend.model import ProjectCreate, ProjectResponse

router = APIRouter()


@router.post("/projects/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = ProjectORM(name=project.name, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.get("/projects/", response_model=list[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return db.query(ProjectORM).all()


@router.get("/projects/{project_id}", response_model=ProjectResponse)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = db.query(ProjectORM).filter(ProjectORM.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = db.query(ProjectORM).filter(ProjectORM.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_project.name = project.name
    db_project.description = project.description
    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/projects/{project_id}", status_code=204)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = db.query(ProjectORM).filter(ProjectORM.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
