from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import inventory, sales, bookings, ai

# Create FastAPI application
app = FastAPI(
    title="Clothing AI Business Backend",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# CORS setup (allows frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(inventory.router)
app.include_router(sales.router)
app.include_router(bookings.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"status": "running", "message": "Clothing AI Backend is live!"}
