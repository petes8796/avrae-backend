from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from db.mongo import db

router = APIRouter(prefix="/applications", tags=["Applications"])

# --- Schema ---
class Application(BaseModel):
    name: str
    email: EmailStr
    occupation: str
    country: str
    networth: str
    reason: str
    socials: str

# --- Routes ---
@router.post("/submit")
async def submit_application(data: Application):
    try:
        collection = db["applications"]
        await collection.insert_one(data.dict())
        return {"status": "success", "message": "Application submitted successfully"}
    except Exception as e:
        print("❌ MongoDB Error:", e)
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/test")
async def test_route():
    return {"status": "ok"}
