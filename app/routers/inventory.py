from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Product
from ..schemas import ProductSchema

router = APIRouter(prefix="/inventory", tags=["inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products", response_model=list[ProductSchema])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).limit(200).all()
