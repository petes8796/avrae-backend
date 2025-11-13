import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError("❌ Missing MONGO_URI environment variable")

try:
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["avrae"]
    applications_collection = db["applications"]
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
