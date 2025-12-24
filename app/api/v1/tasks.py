from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.task import Task, TaskCreate
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Task])
def read_tasks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    tasks = crud.get_tasks(db, skip=skip, limit=limit, owner_id=current_user.id)
    return tasks

@router.post("/", response_model=Task)
def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: TaskCreate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    task = crud.create_user_task(db=db, task=task_in, user_id=current_user.id)
    return task
