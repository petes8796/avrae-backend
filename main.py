from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import applications  # 👈 import your routes folder

app = FastAPI(title="Avrae Backend")

# ✅ Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://avrae-society.com", "https://www.avrae-society.com", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include the applications router
app.include_router(applications.router)

# ✅ Root route (for Render check)
@app.get("/")
def home():
    return {"message": "Avrae Backend is Live"}
