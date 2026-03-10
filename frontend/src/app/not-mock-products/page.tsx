import { revalidatePath } from "next/cache";

type NotMockProduct = {
    id: number;
    category: string;
    brand: string;
    model: string;
    price: number;
    stock: number; 
};

export default async function NotMockProduct() {
    const res = await fetch("http://127.0.0.1:8000/api/products");
    const products = await res.json();

    async function addProduct(formData: FormData) {
        "use server"
        
        const category = formData.get("category")
        const brand = formData.get("brand")
        const model = formData.get("model")
        const price = Number(formData.get("price"))
        const stock = Number(formData.get("stock"))

        const res = await fetch("http://127.0.0.1:8000/api/products", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({category, brand, model, price, stock}),
        });
        const newProduct = await res.json();
        revalidatePath("/not-mock-products");
        console.log(newProduct);
    }

    return (
        <div>
            <form action={addProduct} className="mb-4">
                <input type="text" name="category" required className="border p-2 mr-2 rounded"/>
                <input type="text" name="brand" required className="border p-2 mr-2 rounded"/>
                <input type="text" name="model" required className="border p-2 mr-2 rounded"/>
                <input type="text" name="price" required className="border p-2 mr-2 rounded"/>
                <input type="text" name="stock" required className="border p-2 mr-2 rounded"/>
                <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Add product</button>

            </form>
            <div className="grid grid-cols-4 gap-4 py-10">
                {products.map((product: NotMockProduct) => (
                    <div key={product.id} className="p-4 bg-white shadow-md rounded-lg text-gray-700">
                        <ul><b>{product.brand}</b></ul>
                        <ul>{product.model}</ul>
                        <ul>${product.price}</ul>
                    </div>
                ))}
            </div>
        </div>
    )
     
}