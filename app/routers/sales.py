from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import create_invoice
from ..schemas import InvoiceCreate

router = APIRouter(prefix="/sales", tags=["sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def sales_create(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    try:
        return create_invoice(db, invoice)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
