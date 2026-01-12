# Shop API v4

- v4 setting baseline for testing


## Run tests

From the project root (/shop_api_v4), run:
```
pytest
```


## Firebase Auth. setup

- Create a Firebase project and enable Email/Password authentication  
- Generate a Service Account key and save it as `shop/auth/firebase_credentials.json` (**NEVER** commit this)  
- Create a test user in Firebase Authentication  
- Assign the `"admin"` role using the `set_admin_role.py` script
- Create a Web App in Firebase and save its config to `shop/auth/firebase_config.json` (don't commit this either)


## SQLite setup

Install SQLite - get it from [sqlite.org](https://sqlite.org).  
From `shop/data/`, run:  
```
sqlite3 shop.db < products.sql
```

## Run instructions

```
pip install -r requirements.txt
flask run
```

Once running, open your browser and go to:
- [http://localhost:5000/products](http://localhost:5000/products)
- [http://127.0.0.1:5000/products/p-1001](http://127.0.0.1:5000/products/p-1001)

To update an existing product, send a PUT request with JSON data to `/products/<product_id>` and include your JWT:

```
PUT /products/p-1001
Authorization: Bearer <YOUR_JWT>
Content-Type: application/json

{
    "price": 429.0,
    "in_stock": false
}
```

To delete a product, send a DELETE request:
```
DELETE /products/p-1001
Authorization: Bearer <YOUR_JWT>
```

Protected operations require a valid admin token; missing or invalid tokens return `401`, and non-admin users get `403`.
