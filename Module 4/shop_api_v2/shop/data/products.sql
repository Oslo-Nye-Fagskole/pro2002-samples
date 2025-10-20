BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    currency TEXT NOT NULL,
    in_stock INTEGER NOT NULL CHECK (in_stock IN (0,1))
);

INSERT OR IGNORE INTO products (id, name, price, currency, in_stock) VALUES
    ('p-1001', 'Clean Architecture (Book)', 399.0, 'NOK', 1),
    ('p-2001', 'USB-C Charger 65W', 299.0, 'NOK', 1),
    ('p-3001', 'Wireless Mouse', 249.0, 'NOK', 0);

COMMIT;