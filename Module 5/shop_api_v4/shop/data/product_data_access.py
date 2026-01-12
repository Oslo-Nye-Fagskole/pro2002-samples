# shop/data/product_data_access.py

from typing import List, Optional, Dict, Any
from shop.data.db import connect, rows_to_dicts
from shop.models.product import Product
from shop.models.product_factory import ProductFactory
from shop.models.product_mapper import ProductMapper

class ProductDataAccess:
    """Handles reading and writing product data in the database."""

    def __init__(self, db_path: str | None = None):
        self._db_path = db_path

    def list(self) -> List[Product]:
        """Return all products."""
        with connect(self._db_path) as conn:
            cur = conn.execute("SELECT id, name, price, currency, in_stock FROM products ORDER BY id")
            return [ProductMapper.to_entity(row) for row in rows_to_dicts(cur.fetchall())]

    def get(self, product_id: str) -> Optional[Product]:
        """Return a product by ID."""
        with connect(self._db_path) as conn:
            cur = conn.execute(
                "SELECT id, name, price, currency, in_stock FROM products WHERE id = ?",
                (product_id,),
            )
            row = cur.fetchone()
            return ProductMapper.to_entity(dict(row)) if row else None

    def add(self, payload: Dict[str, Any]) -> Product:
        """Insert a new product."""
        product = ProductFactory.create(payload)
        d = ProductMapper.to_dict(product)
        with connect(self._db_path) as conn:
            conn.execute(
                "INSERT INTO products (id, name, price, currency, in_stock) VALUES (?, ?, ?, ?, ?)",
                (d["id"], d["name"], d["price"], d["currency"], 1 if d["in_stock"] else 0),
            )
            conn.commit()
        return product

    def update(self, product_id: str, payload: Dict[str, Any]) -> Optional[Product]:
        """Update an existing product."""
        current = self.get(product_id)
        if not current:
            return None
        merged = {**ProductMapper.to_dict(current), **payload}
        updated = ProductFactory.create(merged)
        d = ProductMapper.to_dict(updated)
        with connect(self._db_path) as conn:
            conn.execute(
                "UPDATE products SET name = ?, price = ?, currency = ?, in_stock = ? WHERE id = ?",
                (d["name"], d["price"], d["currency"], 1 if d["in_stock"] else 0, product_id),
            )
            conn.commit()
        return updated

    def delete(self, product_id: str) -> bool:
        """Delete a product by ID."""
        with connect(self._db_path) as conn:
            cur = conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
            conn.commit()
            return cur.rowcount > 0
