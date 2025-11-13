from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import applications

app = FastAPI(title="Avrae Backend")

# ✅ Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://avrae-society.com", "https://www.avrae-society.com", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your applications route
app.include_router(applications.router)

# ✅ Simple health check
@app.get("/")
def home():
    return {"message": "Avrae Backend is Live"}
