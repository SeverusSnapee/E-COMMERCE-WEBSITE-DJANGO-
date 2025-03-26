# products/fastapi_app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Sample data
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

app = FastAPI()

# Sample data
products_db = [
    Product(id=1, name="Laptop", description="High-performance laptop", price=999.99),
    Product(id=2, name="Phone", description="Smartphone with high resolution", price=599.99)
]

@app.get("/products/", response_model=List[Product])
def get_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next((product for product in products_db if product.id == product_id), None)
    if product is None:
        return {"error": "Product not found"}
    return product
