from fastapi import FastAPI
from .database import Base, engine
from .routers import inventory, sales, bookings, ai

# Import all models to register them
from . import models
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]  # allow all for now

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clothing AI Business Backend")

app.include_router(inventory.router)
app.include_router(sales.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "Clothing AI Business API is running!"}

