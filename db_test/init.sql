CREATE TABLE IF NOT EXISTS real_estate_data (
    transaction_id UUID PRIMARY KEY,
    transaction_date DATE NOT NULL,
    city VARCHAR(50),
    district VARCHAR(50),
    address VARCHAR(200),
    building_type VARCHAR(50),
    price INTEGER,
    building_area FLOAT,
    unit_price FLOAT,
    floor_level INTEGER,
    building_age FLOAT,
    total_floors INTEGER,
    land_area FLOAT,
    main_use VARCHAR(100),
    construction_materials VARCHAR(100),
    transaction_type VARCHAR(50)
);

CREATE INDEX idx_real_estate_city ON real_estate_data(city);
CREATE INDEX idx_real_estate_district ON real_estate_data(district);
CREATE INDEX idx_real_estate_date ON real_estate_data(transaction_date);
CREATE INDEX idx_real_estate_type ON real_estate_data(building_type);

-- 重新建立 API Key 管理表
DROP TABLE IF EXISTS api_keys;
CREATE TABLE IF NOT EXISTS api_keys (
    id SERIAL PRIMARY KEY,
    key VARCHAR(128) UNIQUE NOT NULL,
    owner VARCHAR(100),
    is_active INTEGER DEFAULT 1,
    usage_count INTEGER DEFAULT 0
);

-- 測試資料
INSERT INTO real_estate_data (
    transaction_id, transaction_date, city, district, address, building_type, price, building_area, unit_price, floor_level, building_age, total_floors, land_area, main_use, construction_materials, transaction_type
) VALUES
('11111111-1111-1111-1111-111111111111', '2024-03-15', '新北市', '板橋區', '中山路一段100號', '大樓', 15000000, 82.5, 181818, 10, 5, 20, 30.0, '住家用', '鋼筋混凝土', '買賣'),
('22222222-2222-2222-2222-222222222222', '2023-12-20', '新北市', '中和區', '景平路200巷5號', '公寓', 9000000, 66.0, 136364, 4, 20, 5, 20.0, '住家用', '加強磚造', '買賣');

-- 測試 API key
INSERT INTO api_keys (key, owner, is_active, usage_count) VALUES
('test-api-key-123', '測試用戶', 1, 0)
ON CONFLICT (key) DO NOTHING;