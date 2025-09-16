import psycopg2

# Ooof...
# The connection string (DSN) is hardcoded here, including database name, user, password, host, and port.
# Any change to this setup requires edits across the codebase, and it ties us tightly to one persistence solution.
# Not to mention the obvious security issue of having user/pwd in clear text...
DB_DSN = "dbname=shop user=shop_admin password=secret host=127.0.0.1 port=5432"

def get_product(product_id):
    # Open a new database connection for each call (inefficient and repeated everywhere).
    conn = psycopg2.connect(DB_DSN)
    cur = conn.cursor()
    # Business logic directly mixed with SQL and schema details.
    # This function "knows" table names, column names, and the exact structure.
    cur.execute("SELECT id, name, price_cents FROM public.products WHERE id = %s", (product_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    # Return is hardcoded to a dict with specific column mapping.
    # No abstraction or reuse, meaning other queries repeat this work.
    return {"id": row[0], "name": row[1], "price_cents": row[2]}

def add_to_cart(user_id, product_id, qty):
    # New connection again (duplicated infrastructure code).
    conn = psycopg2.connect(DB_DSN)
    cur = conn.cursor()
    # PostgreSQL-specific SQL feature: ON CONFLICT.
    # This makes the whole function non-portable to another database.
    cur.execute("""
        INSERT INTO public.carts (user_id) VALUES (%s)
        ON CONFLICT (user_id) DO NOTHING
    """, (user_id,))
    cur.execute("""
        INSERT INTO public.cart_items (user_id, product_id, quantity)
        VALUES (%s, %s, %s)
        ON CONFLICT (user_id, product_id)
        DO UPDATE SET quantity = public.cart_items.quantity + EXCLUDED.quantity
    """, (user_id, product_id, qty))
    conn.commit()
    cur.close()
    conn.close()

def checkout(user_id):
    # Another fresh connection. Imagine this pattern repeated in every function.
    conn = psycopg2.connect(DB_DSN)
    cur = conn.cursor()
    # Total is calculated in raw SQL. This assumes a specific schema, joins, column names, and even money handling logic.
    cur.execute("""
        SELECT SUM(p.price_cents * ci.quantity)
        FROM public.cart_items ci
        JOIN public.products p ON p.id = ci.product_id
        WHERE ci.user_id = %s
    """, (user_id,))
    total_cents = cur.fetchone()[0] or 0
    # Insert directly into orders table.
    # Again, this function "knows" too much about the database schema and persistence details.
    cur.execute("INSERT INTO public.orders (user_id, total_cents) VALUES (%s, %s) RETURNING id", (user_id, total_cents))
    order_id = cur.fetchone()[0]
    # Direct cleanup of cart items here. Business flow and persistence
    # concerns are fully mixed together in a single function.
    cur.execute("DELETE FROM public.cart_items WHERE user_id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return order_id

# Business (domain) logic calls these functions directly, with no abstraction.
# Every feature in the shop depends on psycopg2, SQL dialect details, and schema assumptions. Testing requires a real database.
pid = 101
p = get_product(pid)
if p:
    add_to_cart(user_id=7, product_id=p["id"], qty=2)
    order_id = checkout(user_id=7)
    print(f"Order {order_id} created")