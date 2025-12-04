from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from datetime import datetime
import uuid

# -----------------------------------------------------------------------------
# PRODUCT CRUD
# -----------------------------------------------------------------------------

def list_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def list_variants(db: Session, skip: int = 0, limit: int = 300):
    return db.query(models.ProductVariant).offset(skip).limit(limit).all()

# -----------------------------------------------------------------------------
# INVOICE CREATION LOGIC
# -----------------------------------------------------------------------------

def create_invoice(db: Session, invoice_in: schemas.InvoiceCreate, user_id: str = "SYSTEM"):
    
    # Calculate totals
    total = sum(i.quantity * i.unit_price for i in invoice_in.items)
    discount = invoice_in.discount or 0.0
    net = total - discount

    # Invoice object
    invoice = models.Invoice(
        id=invoice_in.id,
        invoice_no=invoice_in.invoice_no,
        customer_id=invoice_in.customer_id,
        total=total,
        tax=0.0,
        discount=discount,
        net_amount=net,
        status="paid",
        payment_method=invoice_in.payment_method,
        created_at=datetime.utcnow().isoformat(),
        user_id=user_id
    )

    db.add(invoice)

    # Invoice Items + Stock Updates
    for item in invoice_in.items:
        # Create invoice item
        ii = models.InvoiceItem(
            id=str(uuid.uuid4()),
            invoice_id=invoice_in.id,
            variant_id=item.variant_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
            total_price=item.quantity * item.unit_price,
            created_at=datetime.utcnow().isoformat()
        )
        db.add(ii)

        # Fetch stock level — must exist
        stock = db.query(models.StockLevel)\
                  .filter(models.StockLevel.variant_id == item.variant_id)\
                  .first()

        if not stock:
            raise Exception(f"No stock level found for variant {item.variant_id}")

        # Check stock availability
        if stock.quantity_on_hand < item.quantity:
            raise Exception(
                f"Insufficient stock for {item.variant_id} "
                f"(available {stock.quantity_on_hand}, need {item.quantity})"
            )

        # Update stock
        stock.quantity_on_hand -= item.quantity
        stock.last_updated = datetime.utcnow().isoformat()

        # Add stock movement entry
        sm = models.StockMovement(
            id=str(uuid.uuid4()),
            variant_id=item.variant_id,
            change=-item.quantity,
            reason="sale",
            reference_type="invoice",
            reference_id=invoice_in.id,
            seller_id=None,
            user_id=user_id,
            notes=f"Sale invoice {invoice_in.invoice_no}",
            timestamp=datetime.utcnow().isoformat()
        )
        db.add(sm)

    # Final commit
    db.commit()
    db.refresh(invoice)
    return invoice

