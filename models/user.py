from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ApplicationIn(BaseModel):
    name: str
    email: EmailStr
    occupation: Optional[str] = None
    country: Optional[str] = None
    net_worth: Optional[float] = None
    socials: Optional[str] = None
    reason: Optional[str] = None

class ApplicationDB(ApplicationIn):
    payment_status: str = "unpaid"
    application_status: str = "pending"
    created_at: datetime = datetime.utcnow()
