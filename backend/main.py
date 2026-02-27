from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any, Optional
from db import get_connection

app = FastAPI(
    title="Electronics Store API",
    version="2.0.0"
)

# CORS для Next.js (dev режим)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Electronics Store API", "docs": "/docs"}


# ===============================
# GET ALL PRODUCTS
# ===============================
@app.get("/products")
def get_products(category: Optional[str] = Query(None)):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if category:
        cur.execute("SELECT * FROM products WHERE category=%s", (category,))
    else:
        cur.execute("SELECT * FROM products")

    products = cur.fetchall()
    cur.close()
    conn.close()

    return products


# ===============================
# GET SINGLE PRODUCT (WITH DETAILS)
# ===============================
@app.get("/products/{product_id}")
def get_product(product_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    # отримуємо основний продукт
    cur.execute("SELECT * FROM products WHERE id=%s", (product_id,))
    product = cur.fetchone()

    if not product:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")

    # залежно від категорії — робимо JOIN
    if product["category"] == "smartphone":
        cur.execute("""
            SELECT * FROM smartphones WHERE product_id=%s
        """, (product_id,))
        product["details"] = cur.fetchone()

    elif product["category"] == "laptop":
        cur.execute("""
            SELECT * FROM laptops WHERE product_id=%s
        """, (product_id,))
        product["details"] = cur.fetchone()

    elif product["category"] == "smartwatch":
        cur.execute("""
            SELECT * FROM smartwatches WHERE product_id=%s
        """, (product_id,))
        product["details"] = cur.fetchone()

    cur.close()
    conn.close()

    return product


# ===============================
# CREATE PRODUCT + DETAILS
# ===============================
@app.post("/products", status_code=201)
def create_product(data: Dict[str, Any]):

    required_fields = ["category", "brand", "model", "price"]
    for field in required_fields:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"Missing {field}")

    conn = get_connection()
    cur = conn.cursor()

    # 1️⃣ insert into products
    cur.execute("""
        INSERT INTO products (category, brand, model, price, stock, description)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        data["category"],
        data["brand"],
        data["model"],
        data["price"],
        data.get("stock", 0),
        data.get("description", "")
    ))

    product_id = cur.lastrowid

    # 2️⃣ insert into specific table
    if data["category"] == "smartphone":
        cur.execute("""
            INSERT INTO smartphones
            (product_id, display_size, battery_capacity, ram, storage, camera_mp)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            product_id,
            data.get("display_size"),
            data.get("battery_capacity"),
            data.get("ram"),
            data.get("storage"),
            data.get("camera_mp")
        ))

    elif data["category"] == "laptop":
        cur.execute("""
            INSERT INTO laptops
            (product_id, cpu, ram, storage, gpu, screen_size, weight)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            product_id,
            data.get("cpu"),
            data.get("ram"),
            data.get("storage"),
            data.get("gpu"),
            data.get("screen_size"),
            data.get("weight")
        ))

    elif data["category"] == "smartwatch":
        cur.execute("""
            INSERT INTO smartwatches
            (product_id, screen_type, battery_life, water_resistance)
            VALUES (%s,%s,%s,%s)
        """, (
            product_id,
            data.get("screen_type"),
            data.get("battery_life"),
            data.get("water_resistance")
        ))

    else:
        raise HTTPException(status_code=400, detail="Invalid category")

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "created", "id": product_id}


# ===============================
# UPDATE PRODUCT
# ===============================
@app.patch("/products/{product_id}")
def update_product(product_id: int, data: Dict[str, Any]):

    if not data:
        raise HTTPException(status_code=400, detail="No data provided")

    conn = get_connection()
    cur = conn.cursor()

    fields = []
    values = []

    for key, value in data.items():
        fields.append(f"{key}=%s")
        values.append(value)

    sql = f"UPDATE products SET {', '.join(fields)} WHERE id=%s"
    values.append(product_id)

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"status": "updated"}


# ===============================
# DELETE PRODUCT
# ===============================
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM products WHERE id=%s", (product_id,))
    conn.commit()

    cur.close()
    conn.close()

    return {"status": "deleted"}