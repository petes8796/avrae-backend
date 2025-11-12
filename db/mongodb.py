from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("Missing MONGO_URI environment variable")

client = AsyncIOMotorClient(MONGO_URI)
db = client["avrae"]
