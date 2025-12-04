from pydantic import BaseModel
from typing import List, Optional

# -----------------------------------------------------------------------------
# PRODUCT SCHEMAS
# -----------------------------------------------------------------------------

class ProductSchema(BaseModel):
    id: str
    name: str
    category: Optional[str]
    description: Optional[str]
    default_cost_price: Optional[float]
    default_sale_price: Optional[float]
    active: Optional[int]
    created_at: Optional[str]

    class Config:
        from_attributes = True   # replaces orm_mode


class VariantSchema(BaseModel):
    id: str
    product_id: str
    seller_id: Optional[str]
    sku: str
    size: Optional[str]
    color: Optional[str]
    style: Optional[str]
    cost_price: Optional[float]
    sale_price: Optional[float]
    barcode: Optional[str]
    created_at: Optional[str]

    class Config:
        from_attributes = True


# -----------------------------------------------------------------------------
# INVOICE SCHEMAS
# -----------------------------------------------------------------------------

class InvoiceItemCreate(BaseModel):
    variant_id: str
    quantity: int
    unit_price: float


class InvoiceCreate(BaseModel):
    id: str
    invoice_no: str
    customer_id: Optional[str]
    items: List[InvoiceItemCreate]
    discount: Optional[float] = 0.0
    payment_method: Optional[str] = "cash"

    class Config:
        from_attributes = True


# -----------------------------------------------------------------------------
# RESPONSE SCHEMAS
# -----------------------------------------------------------------------------

class InvoiceResponse(BaseModel):
    status: str
    invoice_id: str
    invoice_no: str

    class Config:
        from_attributes = True
