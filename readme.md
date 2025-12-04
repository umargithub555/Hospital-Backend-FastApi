# 🏥 Hospital Management System (FastAPI)

This is a **Hospital Management System API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
It includes **role-based authentication** (Admin, Doctor, Patient) with **JWT tokens** for secure access.

- **Admin** → can create doctors
- **Doctor** → can create patients
- **Patients** → can log in and access their information
- **Email notifications** are sent when a doctor or patient is created

---

## 🚀 Features

- User registration & login with JWT authentication
- Role-based access control (admin, doctor, patient)
- Secure password hashing
- CRUD operations for doctors and patients
- PostgreSQL database integration with SQLAlchemy ORM
- Email notifications on account creation

---

## 📦 Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Auth**: JWT (JSON Web Tokens)
- **Email**: FastAPI Background Tasks + SMTP
- **Environment**: Python 3.12

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/umargithub555/Hospital-Backend-FastApi.git
cd health-backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
uvicorn app.main:app --reload
```
