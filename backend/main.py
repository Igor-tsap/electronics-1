from fastapi import FastAPI, HTTPException, Request
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
def get_products():
    try:
        return Product.all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/api/products")
async def create_product(request: Request):
    try:
        data = await request.json()

        product = Product(
            category=data["category"],
            brand=data["brand"],
            model=data["model"],
            price=data["price"],
            stock=data.get("stock", 0)
        )

        product.save()

        return {"message": "Product created"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))