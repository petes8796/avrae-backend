from fastapi import APIRouter, BackgroundTasks
from models.user import ApplicationIn
from db.mongo import applications
from utils.emailer import send_new_application_email
from datetime import datetime

router = APIRouter()

@router.post("/submit")
async def submit_application(payload: ApplicationIn, background_tasks: BackgroundTasks):
    doc = payload.dict()
    doc.update({
        "payment_status": "unpaid",
        "application_status": "pending",
        "created_at": datetime.utcnow()
    })
    res = await applications.insert_one(doc)
    app_id = str(res.inserted_id)
    background_tasks.add_task(send_new_application_email, app_id, doc)
    return {"id": app_id, "status": "created", "message": "Application received. Pending review."}
