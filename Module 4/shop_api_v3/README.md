# Shop API v3

- v3 with Firebase Authentication

## Firebase Auth. setup
TODO

## SQLite setup  
Install SQLite - get it from [sqlite.org](https://sqlite.org).  
From `shop/data/`, run:  
```bash
sqlite3 shop.db < products.sql
```

## Run instructions

```bash
pip install -r requirements.txt
flask run
```

Once running, open your browser and go to:
- [http://localhost:5000/products](http://localhost:5000/products)
- [http://127.0.0.1:5000/products/p-1001](http://127.0.0.1:5000/products/p-1001)

To update an existing product, send a PUT request with JSON data to `/products/<product_id>`:

```
PUT /products/p-1001
Content-Type: application/json
{
"price": 429.0,
"in_stock": false
}
```

To delete a product, send a DELETE request:
```
DELETE /products/p-1001
```

Both operations return appropriate HTTP status codes (**200** for update, **204** for delete) confirming successful completion. To view and confirm the changes above, access the full product list after each to see the difference.

With SQLite database now, all changes made through the API are persisted.
