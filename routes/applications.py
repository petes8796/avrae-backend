from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.mongo import db  # ✅ use global DB connection from mongo.py

router = APIRouter(prefix="/applications", tags=["Applications"])

# --- Schema ---
class Application(BaseModel):
    name: str
    email: str
    occupation: str
    country: str
    networth: str
    reason: str
    socials: str


@router.post("/submit")
async def submit_application(data: Application):
    try:
        # Insert into the "applications" collection in the "avrae" DB
        result = await db["applications"].insert_one(data.dict())

        if not result.inserted_id:
            raise HTTPException(status_code=500, detail="Insert failed")

        return {"status": "success", "message": "Application submitted successfully."}

    except Exception as e:
        print("❌ Error saving application:", e)
        raise HTTPException(status_code=500, detail="Database error")


@router.get("/test")
async def test_route():
    return {"status": "ok"}
