

INSERT INTO products (category, brand, model, price, stock, ram, storage, display_size, battery_capacity, camera_mp, cpu, gpu, screen_size, weight, screen_type, battery_life, water_resistance, description)
VALUES
-- Smartphones (10)
('smartphone', 'Apple', 'iPhone 15', 1200.00, 10, 8, 256, 6.1, 3279, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Latest Apple smartphone.'),
('smartphone', 'Apple', 'iPhone 15 Pro', 1400.00, 5, 8, 512, 6.1, 3279, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Pro version of iPhone 15.'),
('smartphone', 'Samsung', 'Galaxy S23', 999.00, 15, 12, 512, 6.2, 3900, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Flagship Samsung phone.'),
('smartphone', 'Samsung', 'Galaxy S23+', 1099.00, 8, 12, 512, 6.7, 4700, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Large-screen Samsung flagship.'),
('smartphone', 'Google', 'Pixel 8', 899.00, 12, 8, 256, 6.2, 4000, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Google Pixel with pure Android.'),
('smartphone', 'OnePlus', '10 Pro', 799.00, 7, 12, 256, 6.7, 5000, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'High-performance OnePlus phone.'),
('smartphone', 'Xiaomi', '12S Ultra', 950.00, 9, 12, 512, 6.7, 4860, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Xiaomi flagship smartphone.'),
('smartphone', 'Sony', 'Xperia 1 IV', 1200.00, 4, 12, 256, 6.5, 5000, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Sony smartphone with 4K screen.'),
('smartphone', 'Huawei', 'P60 Pro', 850.00, 6, 8, 256, 6.6, 4800, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Huawei flagship smartphone.'),
('smartphone', 'Motorola', 'Edge 40', 700.00, 10, 8, 256, 6.6, 4200, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Motorola mid-range phone.'),

-- Laptops (10)
('laptop', 'Dell', 'XPS 15', 2000.00, 5, 16, 512, NULL, NULL, NULL, 'Intel i7', 'NVIDIA RTX 4050', 15.6, 1.8, NULL, NULL, NULL, 'High-performance laptop.'),
('laptop', 'Dell', 'XPS 17', 2500.00, 3, 32, 1024, NULL, NULL, NULL, 'Intel i9', 'NVIDIA RTX 4060', 17.0, 2.1, NULL, NULL, NULL, 'Large Dell laptop for professionals.'),
('laptop', 'Apple', 'MacBook Pro 14', 2400.00, 4, 16, 512, NULL, NULL, NULL, 'Apple M2 Pro', 'Integrated', 14.2, 1.6, NULL, NULL, NULL, 'Apple laptop with M2 Pro chip.'),
('laptop', 'Apple', 'MacBook Pro 16', 3000.00, 3, 32, 1024, NULL, NULL, NULL, 'Apple M2 Max', 'Integrated', 16.0, 2.1, NULL, NULL, NULL, 'Professional Apple laptop.'),
('laptop', 'Lenovo', 'ThinkPad X1 Carbon', 1800.00, 6, 16, 512, NULL, NULL, NULL, 'Intel i7', 'Integrated', 14.0, 1.2, NULL, NULL, NULL, 'Business ultrabook.'),
('laptop', 'HP', 'Spectre x360', 1700.00, 5, 16, 512, NULL, NULL, NULL, 'Intel i7', 'Integrated', 13.5, 1.3, NULL, NULL, NULL, 'Convertible laptop.'),
('laptop', 'Asus', 'ROG Strix G15', 1600.00, 4, 16, 1024, NULL, NULL, NULL, 'AMD Ryzen 7', 'NVIDIA RTX 4060', 15.6, 2.0, NULL, NULL, NULL, 'Gaming laptop.'),
('laptop', 'Acer', 'Predator Helios 300', 1500.00, 6, 16, 512, NULL, NULL, NULL, 'Intel i7', 'NVIDIA RTX 3060', 15.6, 2.2, NULL, NULL, NULL, 'Mid-range gaming laptop.'),
('laptop', 'MSI', 'GF65 Thin', 1400.00, 5, 16, 512, NULL, NULL, NULL, 'Intel i7', 'NVIDIA RTX 3060', 15.6, 1.9, NULL, NULL, NULL, 'Lightweight gaming laptop.'),
('laptop', 'Razer', 'Blade 15', 2500.00, 2, 32, 1024, NULL, NULL, NULL, 'Intel i9', 'NVIDIA RTX 4070', 15.6, 2.0, NULL, NULL, NULL, 'Premium gaming laptop.'),

-- Smartwatches (10)
('smartwatch', 'Apple', 'Watch Series 9', 399.00, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'OLED', 18, '50m', 'Latest Apple smartwatch.'),
('smartwatch', 'Apple', 'Watch SE', 249.00, 25, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'OLED', 20, '50m', 'Affordable Apple watch.'),
('smartwatch', 'Samsung', 'Galaxy Watch 6', 349.00, 12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AMOLED', 20, '50m', 'Flagship Samsung smartwatch.'),
('smartwatch', 'Samsung', 'Galaxy Watch 6 Classic', 399.00, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AMOLED', 25, '50m', 'Samsung classic smartwatch.'),
('smartwatch', 'Garmin', 'Venu 2', 299.00, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AMOLED', 15, '50m', 'Garmin fitness watch.'),
('smartwatch', 'Fitbit', 'Versa 4', 199.00, 18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'OLED', 14, '50m', 'Fitbit health smartwatch.'),
('smartwatch', 'Huawei', 'Watch GT 3', 229.00, 12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AMOLED', 21, '50m', 'Huawei smartwatch.'),
('smartwatch', 'Amazfit', 'GTR 4', 179.00, 14, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AMOLED', 18, '50m', 'Amazfit smartwatch.'),
('smartwatch', 'Garmin', 'Fenix 7', 599.00, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Transflective', 24, '100m', 'Premium Garmin watch.'),
('smartwatch', 'Samsung', 'Galaxy Watch 5', 299.00, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AMOLED', 16, '50m', 'Previous generation Samsung watch.');