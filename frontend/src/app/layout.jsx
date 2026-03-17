import { Roboto, Inter } from "next/font/google";
import "./globals.css";
import Header from "./components/Header";

const roboto = Roboto({
  variable: "--font-roboto",
  subsets: ["latin"],
  weight: ["400", "500", "700"], // optional: specify weights you need
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  weight: ["400", "500", "700"], // optional
});

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body className={`${roboto.variable} ${inter.variable}`}>
                <Header />
                {children}
            </body>
        </html>
    );
}