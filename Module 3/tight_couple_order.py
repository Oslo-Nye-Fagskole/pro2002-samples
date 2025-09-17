class Order:
    def __init__(self, user, db):
        # Here the Order class directly relies on the internal structure of User.
        # It assumes that User has both "id" and "email" attributes.
        # If the User model changes (for example, renaming "email" to "contact") this code will immediately break.
        self.user_id = user.id
        self.user_email = user.email

        # The database object is passed in directly.
        # Order now also has to know how to talk to the database instead of just handling business rules.
        self.db = db

    def save(self, items):
        # Again: business logic (placing an order) is mixed with persistence details.
        # This SQL string assumes a specific database schema with exact table and column names.
        self.db.execute(
            "INSERT INTO orders (user_id, email) VALUES (?, ?)",
            (self.user_id, self.user_email)
        )

        # For each item, more direct SQL is written here.
        # The class now depends on the existence of an "order_items" table,
        # specific column names, and even how product and quantity are stored.
        # The "123" order_id is hardcoded, showing how brittle this setup is.
        # (yes I know, a stupid example with the hardcoded "123", but it's there to prove a point.
        # you won't believe how often things like this occur in real software!)
        for item in items:
            self.db.execute(
                "INSERT INTO order_items (order_id, product, qty) VALUES (?, ?, ?)",
                (123, item.name, item.qty)  # tightly bound to schema and naming
            )