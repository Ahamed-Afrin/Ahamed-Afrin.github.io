from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from ..models.task import Task, TaskStatus
from ..schemas.task import TaskCreate, TaskUpdate


class TaskService:
    """Service for task operations"""

    @staticmethod
    def create_task(db: Session, task_data: TaskCreate, user_id: int) -> Task:
        """
        Create a new task for a user

        Args:
            db: Database session
            task_data: Task creation data
            user_id: ID of the user creating the task

        Returns:
            Created Task object
        """
        db_task = Task(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            user_id=user_id
        )

        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def get_tasks(
            db: Session,
            user_id: int,
            status: Optional[TaskStatus] = None,
            search: Optional[str] = None
    ) -> List[Task]:
        """
        Get all tasks for a user with optional filtering

        Args:
            db: Database session
            user_id: User ID
            status: Optional status filter
            search: Optional search query for title/description

        Returns:
            List of Task objects
        """
        query = db.query(Task).filter(Task.user_id == user_id)

        # Apply status filter if provided
        if status:
            query = query.filter(Task.status == status)

        # Apply search filter if provided
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(
                (Task.title.ilike(search_pattern)) |
                (Task.description.ilike(search_pattern))
            )

        return query.order_by(Task.created_at.desc()).all()

    @staticmethod
    def get_task_by_id(db: Session, task_id: int, user_id: int) -> Task:
        """
        Get a specific task by ID for a user

        Args:
            db: Database session
            task_id: Task ID
            user_id: User ID

        Returns:
            Task object

        Raises:
            HTTPException: If task not found or doesn't belong to user
        """
        task = db.query(Task).filter(
            Task.id == task_id,
            Task.user_id == user_id
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return task

    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int) -> Task:
        """
        Update a task

        Args:
            db: Database session
            task_id: Task ID
            task_data: Task update data
            user_id: User ID

        Returns:
            Updated Task object

        Raises:
            HTTPException: If task not found or doesn't belong to user
        """
        task = TaskService.get_task_by_id(db, task_id, user_id)

        # Update fields if provided
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.status is not None:
            task.status = task_data.status

        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db: Session, task_id: int, user_id: int) -> None:
        """
        Delete a task

        Args:
            db: Database session
            task_id: Task ID
            user_id: User ID

        Raises:
            HTTPException: If task not found or doesn't belong to user
        """
        task = TaskService.get_task_by_id(db, task_id, user_id)
        db.delete(task)
        db.commit()