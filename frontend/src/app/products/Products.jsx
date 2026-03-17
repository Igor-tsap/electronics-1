export default async function Products() {
    const res = await fetch("http://127.0.0.1:8000/api/products", {
        cache: "no-store",
    });

    if (!res.ok) {
        throw new Error("Failed to fetch products");
    }

    const products = await res.json();

    return (
        <ul className="space-y-4 p-4">
            {products.map((product) => (
                <li key={product.id}>
                    {product.brand} {product.model} {product.price}
                </li>
            ))}
        </ul>

    );
}