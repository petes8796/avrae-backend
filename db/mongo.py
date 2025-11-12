import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise Exception("MONGO_URI not found. Please set it in Render environment variables.")

client = AsyncIOMotorClient(MONGO_URI)
db = client["avrae"]  # your database name
applications_collection = db.get_collection("applications")
