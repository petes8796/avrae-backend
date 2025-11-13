from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.mongo import applications_collection

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
        result = await applications_collection.insert_one(data.dict())
        return {"status": "success", "id": str(result.inserted_id)}
    except Exception as e:
        print("❌ Error saving application:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/test")
async def test_route():
    return {"status": "ok"}
