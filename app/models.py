from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
from .database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, nullable=False)
    employee_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)  # present, absent, or leave
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
