from fastapi import FastAPI, HTTPException
from .models import Product
from .db import get_connection

app = FastAPI()


@app.get("/api/products")
def get_products():
    try:
        return Product.all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))