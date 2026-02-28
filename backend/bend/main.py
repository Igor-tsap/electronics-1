# # from fastapi import FastAPI, HTTPException
# # from fastapi.middleware.cors import CORSMiddleware
# # from typing import Optional
# # import mysql.connector
# # from mysql.connector import Error
# # from pydantic import BaseModel
# # from models import Product
# # from db import get_connection

# # app = FastAPI()

# # origins = [
# #     "http://localhost:3000",
# #     "http://localhost",
# #     "http://localhost:5000",
# # ]

# # products = Product.all()
# # print("All products in DB:")
# # for p in products:
# #     print(p)
# from models import Product


# products = Product.all()
# for prod in products:
#     print(prod)

# # @app.get("/api/products")
# # def get_products():
# #     return Product.all()

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