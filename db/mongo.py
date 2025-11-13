import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError("Missing MONGO_URI environment variable")

client = AsyncIOMotorClient(MONGO_URI)
db = client["avrae"]  # Your database name
