import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI not found. Add it in Render Environment Variables.")

try:
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.get_default_database()  # auto-uses "avrae"
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
    raise
