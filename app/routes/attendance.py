from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create attendance record
@router.post("/", response_model=schemas.AttendanceResponse)
def create_attendance(data: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.create_attendance(db, data)

# Get all records (with optional search/sort/filter)
@router.get("/", response_model=List[schemas.AttendanceResponse])
def get_all_attendance(
    search: Optional[str] = None,
    sortBy: Optional[str] = Query(default=None, regex="^(employee_name|date|status)$"),
    order: Optional[str] = Query(default="asc", regex="^(asc|desc)$"),
    status: Optional[str] = Query(default=None, regex="^(present|absent|leave)$"),
    date: Optional[str] = Query(default=None, regex="^(today|past|future)$"),
    db: Session = Depends(get_db)
):
    return crud.get_all_attendance(db, search, sortBy, order, status, date)

# Get single record
@router.get("/{attendance_id}", response_model=schemas.AttendanceResponse)
def get_attendance(attendance_id: int, db: Session = Depends(get_db)):
    record = crud.get_attendance(db, attendance_id)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return record

# Update attendance record
@router.put("/{attendance_id}", response_model=schemas.AttendanceResponse)
def update_attendance(attendance_id: int, updates: schemas.AttendanceUpdate, db: Session = Depends(get_db)):
    record = crud.update_attendance(db, attendance_id, updates)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return record

# Delete record
@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    record = crud.delete_attendance(db, attendance_id)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return {"message": "Record deleted successfully"}
