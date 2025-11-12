import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI not found. Add it in your Render environment variables.")

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_default_database() or client["avrae"]

applications = db.get_collection("applications")
