from fastapi import FastAPI, HTTPException, Query, Request
from models import Product
from fastapi.middleware.cors import CORSMiddleware
# from .db import get_connection

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
def get_products(page: int = Query(1), limit: int = Query(10)):
    try:
        return Product.paginate(page, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
