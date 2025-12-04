from sqlalchemy import Column, String, Integer, Float, Text
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(Text)
    default_cost_price = Column(Float)
    default_sale_price = Column(Float)
    active = Column(Integer)
    created_at = Column(String)


class ProductVariant(Base):
    __tablename__ = "product_variants"
    id = Column(String, primary_key=True)
    product_id = Column(String)
    seller_id = Column(String)
    sku = Column(String)
    size = Column(String)
    color = Column(String)
    style = Column(String)
    cost_price = Column(Float)
    sale_price = Column(Float)
    barcode = Column(String)
    created_at = Column(String)
