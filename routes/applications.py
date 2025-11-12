from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.mongodb import db  # clean import

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
        await db["applications"].insert_one(data.dict())
        return {"status": "success"}
    except Exception as e:
        print("Error saving application:", e)
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/test")
async def test_route():
    return {"status": "ok"}
