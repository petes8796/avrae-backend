from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.mongo import applications_collection

router = APIRouter()

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
        result = await applications_collection.insert_one(data.dict())
        if result.inserted_id:
            return {"status": "success"}
        raise Exception("Insert failed")
    except Exception as e:
        print("Error saving application:", e)
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/test")
async def test_route():
    return {"status": "ok"}
