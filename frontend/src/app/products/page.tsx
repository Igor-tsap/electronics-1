"use client"
import { useState, useEffect } from "react";

type Product = {
    id: number;
    brand: string;
    model: string;
    price: number;
    stock: number; 
};

export default function Products() {
    const [products, setProducts] = useState<Product[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        async function fetchProducts() {
            try {
                const response = await fetch(
                    "http://127.0.0.1:8000/api/products"
                );
                if (!response.ok) {
                    throw new Error("Failed to fetch products");
                }
                const data = await response.json();
                setProducts(data);
            } catch (err) {
                setError("Failed to fetch products");
                if (err instanceof Error) {
                    setError(`Failed to fetch products: ${err.message}`);
                }
            } finally {
                setLoading(false);
            }
        };
        fetchProducts();
    }, []);
    return (
        <ul className="space-y-4 p-4">
            {products.map((product) => (
                <li key={product.id} className="p-4 bg-white shadow-md rounded-lg text-gray-700">
                    {product.brand} ({product.model})
                </li>
            ))}
        </ul>
    );
};
