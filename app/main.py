from fastapi import FastAPI
from .database import Base, engine
from .routers import inventory, sales, bookings, ai

# Import all models to register them
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clothing AI Business Backend")

app.include_router(inventory.router)
app.include_router(sales.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "Clothing AI Business API is running!"}
