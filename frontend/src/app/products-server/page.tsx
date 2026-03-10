type Product = {
    id: number;
    brand: string;
    model: string;
    price: number;
    stock: number; 
};

export default async function ProductsSever() {
    const res = await fetch("http://127.0.0.1:8000/api/products");
    const products = await res.json();

    return (
        <ul className="space-y-4 p-4">
            {products.map((product: Product) => (
                <li key={product.id} className="p-4 bg-white shadow-md rounded-lg text-gray-700">
                    {product.brand} {product.model}
                </li>
            ))}
        </ul>
    );
}