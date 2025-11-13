from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import applications

app = FastAPI()

# ✅ FULL CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- temporarily allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(applications.router)

@app.get("/")
async def root():
    return {"message": "Avrae Backend is Live"}
