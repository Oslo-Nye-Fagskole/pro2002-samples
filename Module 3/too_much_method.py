# A long method doing far too many things at once
# What do we do if any one or more of these operations fail?
# How do you even test this?!?
def process_order(order, user, discount_code, db, notify):

    # Step 1: Calculate total
    # Calculation logic mixed directly into the order processing
    total = 0
    for item in order.items:
        total += item.price * item.qty

    # Step 2: Apply discount
    # Discount logic hardcoded with magic numbers
    # What if we add other discounts? Do we keep stacking elifs forever?
    if discount_code == "VIP":
        total = total * 0.8
    elif discount_code == "FREESHIP":
        total = total - 50

    # Step 3: Persist order
    # SQL in the middle of business logic
    # Ask yourself: Should this method really know the exact database schema?
    db.execute("INSERT INTO orders (user, total) VALUES (?, ?)", (user, total))

    # Step 4: Notify user
    # What happens if notification rules change, or we add like SMS or some other way to notify?
    if notify:
        print(f"Email sent to {user.email}: Your order total is {total}")
