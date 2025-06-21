from fastapi import FastAPI
from .database import Base, engine
from .routes import attendance

app = FastAPI(
    title="Attendance Management API",
    description="Track employee attendance with filtering, sorting, and search.",
    version="1.0.0"
)

# Create DB tables from models
Base.metadata.create_all(bind=engine)

# Register the attendance routes
app.include_router(attendance.router)

Base.metadata.create_all(bind=engine)
