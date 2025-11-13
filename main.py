from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# --- Ensure 'routes' folder is importable even on Render ---
sys.path.append(os.path.join(os.path.dirname(__file__), "routes"))

from routes import applications  # ✅ this must work

app = FastAPI(title="Avrae Backend")

# --- CORS setup ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://avrae-society.com", "https://www.avrae-society.com", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routes ---
app.include_router(applications.router)

@app.get("/")
def home():
    return {"message": "Avrae Backend is Live"}
