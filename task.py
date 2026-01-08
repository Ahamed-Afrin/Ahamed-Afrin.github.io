from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from ..models.task import TaskStatus


class TaskBase(BaseModel):
    """Base task schema with common fields"""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING


class TaskCreate(TaskBase):
    """Schema for task creation"""
    pass


class TaskUpdate(BaseModel):
    """Schema for task update"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskResponse(TaskBase):
    """Schema for task response"""
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True