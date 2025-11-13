from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import applications  # adjust if you have different folder name

app = FastAPI()

# ✅ Allow your frontend domain
origins = [
    "https://avrae-society.com",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ include your routes
app.include_router(applications.router)

@app.get("/")
async def root():
    return {"message": "Avrae Backend is Live"}
