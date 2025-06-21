from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

# Base schema: used for both Create and Response
class AttendanceBase(BaseModel):
    employee_id: str
    employee_name: str
    date: date
    status: str
    notes: Optional[str] = None

# For creating a new record
class AttendanceCreate(AttendanceBase):
    pass

# For updating an existing record
class AttendanceUpdate(BaseModel):
    date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None

# For returning data from API (includes ID and created_at)
class AttendanceResponse(AttendanceBase):
    id: int
    created_at: datetime

    class Config:

        from_attributes = True
 # Allows SQLAlchemy models to be converted to Pydantic models
