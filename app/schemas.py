from pydantic import BaseModel
from typing import Optional, List

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
        orm_mode = True
