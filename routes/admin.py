from fastapi import APIRouter, Header, HTTPException
from db.mongo import applications
from bson import ObjectId
import os

router = APIRouter()

def verify_admin(secret: str):
    expected = os.getenv("ADMIN_SECRET")
    return secret and expected and secret == expected

@router.get("/pending")
async def pending_applications(x_admin_secret: str = Header(None)):
    if not verify_admin(x_admin_secret):
        raise HTTPException(status_code=401, detail="Unauthorized")
    docs = []
    cursor = applications.find({"application_status": "pending"}).sort("created_at", -1).limit(100)
    async for doc in cursor:
        doc["id"] = str(doc.pop("_id"))
        docs.append(doc)
    return docs

@router.post("/approve/{app_id}")
async def approve_application(app_id: str, x_admin_secret: str = Header(None)):
    if not verify_admin(x_admin_secret):
        raise HTTPException(status_code=401, detail="Unauthorized")
    res = await applications.update_one({"_id": ObjectId(app_id)}, {"$set": {"application_status": "approved"}})
    if res.modified_count:
        return {"status": "approved", "id": app_id}
    return {"status": "not_found"}

@router.post("/reject/{app_id}")
async def reject_application(app_id: str, x_admin_secret: str = Header(None)):
    if not verify_admin(x_admin_secret):
        raise HTTPException(status_code=401, detail="Unauthorized")
    res = await applications.update_one({"_id": ObjectId(app_id)}, {"$set": {"application_status": "rejected"}})
    if res.modified_count:
        return {"status": "rejected", "id": app_id}
    return {"status": "not_found"}
