"use client"
import { useRouter } from "next/navigation";

export default function About() {
    const router = useRouter();
    return (
        <div>
            <h1>About us</h1>
            <button
                onClick={() => router.push("/")}
                className="bg-blue-500 text-white p-2 rounded-md"
            >
                Go home
            </button>
        </div>
        
    );
}