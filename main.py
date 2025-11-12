from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import applications

# Initialize FastAPI app
app = FastAPI(title="Avrae Backend API")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with ['https://avrae-society.com'] for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(applications.router)

# Health check route
@app.get("/")
def root():
    return {"status": "Avrae backend running successfully"}
