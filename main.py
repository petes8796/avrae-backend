from fastapi import FastAPI
from routes import applications

app = FastAPI()

# Register router
app.include_router(applications.router, prefix="/applications", tags=["applications"])

@app.get("/")
def home():
    return {"message": "Avrae Backend is Live"}
