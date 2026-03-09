CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- загальні поля
    category ENUM('smartphone','laptop','smartwatch') NOT NULL,
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(150) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- smartphone fields
    display_size DECIMAL(3,1) NULL,
    battery_capacity INT NULL,
    camera_mp INT NULL,

    -- laptop fields
    cpu VARCHAR(100) NULL,
    gpu VARCHAR(100) NULL,
    screen_size DECIMAL(3,1) NULL,
    weight DECIMAL(4,2) NULL,

    -- smartwatch fields
    screen_type VARCHAR(50) NULL,
    battery_life INT NULL,
    water_resistance VARCHAR(50) NULL,

    -- shared optional specs
    ram INT NULL,
    storage INT NULL
);