import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI not found. Add it in Render Environment Variables.")

client = AsyncIOMotorClient(MONGO_URI)
db = client["avrae"]
applications_collection = db["applications"]
