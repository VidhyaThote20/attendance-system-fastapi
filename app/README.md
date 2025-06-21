
# 📝 Attendance Management API – FastAPI + PostgreSQL

This is a full-featured **Attendance Management System API** built using FastAPI, SQLAlchemy, and PostgreSQL.  
It supports CRUD operations on employee attendance and includes powerful features like search, sorting, and filtering — all easily testable through Swagger UI.

---

## 📦 Tech Stack

- ⚙️ **FastAPI** – Web framework for building APIs
- 🐘 **PostgreSQL** – Relational database
- 🧠 **SQLAlchemy** – ORM for handling database models
- 🧾 **Pydantic** – Data validation and serialization
- 🔥 **Uvicorn** – ASGI server to run FastAPI
- 💾 **pgAdmin 4** – GUI for PostgreSQL management

---

## 📁 Project Structure

```
attendance-system-fastapi/
├── app/
│   ├── main.py             # FastAPI entry point
│   ├── database.py         # DB connection and engine
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic request/response schemas
│   ├── crud.py             # DB operation logic
│   └── routes/
│       └── attendance.py   # All API endpoints
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 📌 Prerequisites
- Python 3.10+
- PostgreSQL
- pgAdmin 4 (optional but recommended)

### 🚀 Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/attendance-system-fastapi.git
cd attendance-system-fastapi
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL database**
- Create a PostgreSQL database named: `attendance_db`
- Update your connection URL in `app/database.py`:
```python
DATABASE_URL = "postgresql://postgres:<your-password>@localhost/attendance_db"
```

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

6. **Open Swagger Docs to Test API**
Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ API Features

### ➕ POST `/attendance`
- Create a new attendance record
```json
{
  "employee_id": "EMP001",
  "employee_name": "Jhon",
  "date": "2025-06-19",
  "status": "present",
  "notes": "Arrived on time"
}
```

### 📥 GET `/attendance`
- Get all records
- Supports:
  - `search` → by name or notes
  - `sortBy` → `employee_name`, `date`, `status`
  - `order` → `asc`, `desc`
  - `status` → `present`, `absent`, `leave`
  - `date` → `today`, `past`, `future`

### 🔍 Example:
```
/attendance?search=vidhya&sortBy=date&order=desc&status=present
```

### 📄 GET `/attendance/{id}`
- Get a specific record by ID

### ✏️ PUT `/attendance/{id}`
- Update the status, date, or notes of a record

### ❌ DELETE `/attendance/{id}`
- Delete an attendance record

---

## 🧪 Testing via Swagger

FastAPI provides interactive Swagger docs at:
```
http://127.0.0.1:8000/docs
```
Use this UI to send test requests without needing Postman.

---

## 📎 Assignment Notes

- [x] ✔️ Repository name: `attendance-system-fastapi`
- [x] ✔️ Code structured and modular
- [x] ✔️ Clean API docs with examples
- [x] ✔️ GitHub-hosted with `README.md` and working code
