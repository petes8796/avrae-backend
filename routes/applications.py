# routes/applications.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.mongo import db
import traceback

router = APIRouter(prefix="/applications", tags=["Applications"])

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
        result = await db["applications"].insert_one(data.dict())
        return {"status": "success", "id": str(result.inserted_id)}
    except Exception as e:
        tb = traceback.format_exc()
        print("❌ Error saving application:\n", tb)   # will appear in Render logs
        # return a generic error to client
        raise HTTPException(status_code=500, detail="Server error (check backend logs)")
