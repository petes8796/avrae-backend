from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

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
    # TEMPORARY: do not write to DB, just echo back — tests connectivity only
    try:
        return {"status": "success", "received": data.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")

@router.get("/test")
async def test_route():
    return {"status": "ok"}
