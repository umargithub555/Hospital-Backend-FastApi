from fastapi import FastAPI

from .db import models
from .db.connection import engine
from app.routers import admin,patient,doctor,chatbot
from .auth import registration
from app.db.connection import SessionLocal
from app.db.models import User
from app.utils.utils import hash_password




models.Base.metadata.create_all(bind=engine)




app = FastAPI()



app.include_router(admin.router)
app.include_router(registration.router)
app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(chatbot.router)



@app.get("/")
def hello():
    return {"message":"everything well"}






@app.post("/seed-admin")
def seed_admin():
    db = SessionLocal()
    existing_admin = db.query(User).filter(User.role == "admin").first()
    if not existing_admin:
        admin = User(
            username="superadmin",
            email="admin@example.com",
            password=hash_password("admin123"),
            role="admin"
        )
        db.add(admin)
        db.commit()
        print("✅ Admin created")
    else:
        print("⚠️ Admin already exists")
    db.close()