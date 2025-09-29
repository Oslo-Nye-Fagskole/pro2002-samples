# discounts.py
def final_price(items, tax=0.25, discount=0.1):
    total = 0
    for it in items:
        subtotal = it.price_cents * it.qty
    if subtotal > 1000:
        subtotal = int(subtotal * (1 - discount))
    total += subtotal
    total = int(total * (1 + tax))
    return total
