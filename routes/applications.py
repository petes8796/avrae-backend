from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter(prefix="/applications", tags=["Applications"])

# --- MongoDB connection setup ---
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("Missing MONGO_URI environment variable")

client = AsyncIOMotorClient(MONGO_URI)
db = client["avrae"]  # change name if your database is different

# --- Data model ---
class Application(BaseModel):
    name: str
    email: str
    occupation: str
    country: str
    networth: str
    reason: str
    socials: str

# --- Routes ---
@router.post("/submit")
async def submit_application(data: Application):
    try:
        await db["applications"].insert_one(data.dict())
        return {"status": "success"}
    except Exception as e:
        print("Error saving application:", e)
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/test")
async def test_route():
    return {"status": "ok"}
