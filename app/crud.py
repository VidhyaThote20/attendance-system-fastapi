from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import date, datetime
from . import models, schemas

# CREATE
def create_attendance(db: Session, data: schemas.AttendanceCreate):
    attendance = models.Attendance(**data.dict())
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

# READ ALL (with optional search, sort, filter)
def get_all_attendance(db: Session, search: str = None, sort_by: str = None, order: str = "asc", status: str = None, date_filter: str = None):
    query = db.query(models.Attendance)

    if search:
        query = query.filter(
            or_(
                models.Attendance.employee_name.ilike(f"%{search}%"),
                models.Attendance.notes.ilike(f"%{search}%")
            )
        )

    if status:
        query = query.filter(models.Attendance.status == status)

    if date_filter == "today":
        query = query.filter(models.Attendance.date == date.today())
    elif date_filter == "past":
        query = query.filter(models.Attendance.date < date.today())
    elif date_filter == "future":
        query = query.filter(models.Attendance.date > date.today())

    if sort_by:
        sort_column = getattr(models.Attendance, sort_by, None)
        if sort_column is not None:
            if order == "desc":
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())

    return query.all()

# READ ONE
def get_attendance(db: Session, attendance_id: int):
    return db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()

# UPDATE
def update_attendance(db: Session, attendance_id: int, updates: schemas.AttendanceUpdate):
    attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if not attendance:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(attendance, key, value)
    db.commit()
    db.refresh(attendance)
    return attendance

# DELETE
def delete_attendance(db: Session, attendance_id: int):
    attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if not attendance:
        return None
    db.delete(attendance)
    db.commit()
    return attendance
