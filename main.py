from fastapi import FastAPI
from routes import applications

app = FastAPI(title="Avrae Backend", version="1.0.0")

# Register router
app.include_router(applications.router, prefix="/applications", tags=["Applications"])

@app.get("/")
async def root():
    return {"message": "Avrae Backend is Live"}
