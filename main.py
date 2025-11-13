from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import applications

app = FastAPI()

# ✅ CORS FIX
origins = [
    "https://avrae-society.com",  # your frontend domain
    "http://localhost:3000",      # for local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routers
app.include_router(applications.router)

@app.get("/")
async def root():
    return {"message": "Avrae Backend is Live"}
