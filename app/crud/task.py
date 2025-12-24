from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def get_tasks(db: Session, skip: int = 0, limit: int = 100, owner_id: int = 1):
    return db.query(Task).filter(Task.owner_id == owner_id).offset(skip).limit(limit).all()

def create_user_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.model_dump(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
