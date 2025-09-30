# legacy_shop_improved_v2.py -> Factory and Strategy pattern improvement

from item_factory import make_item
from discounts_strategy import default_discount_strategy

TAX_RATE = 0.25
DISCOUNTS = default_discount_strategy()  # injected strategy (behavior unchanged)

def load_cart(raw_items):
    cart = []
    for it in raw_items:
        obj = make_item(it)
        if obj is not None:
            cart.append(obj)
        else:
            # Unknown type still silently ignored: fragile, hard to debug.
            pass
    return cart

def add_promotional_item(cart, user_tier):
    # Reuses the same factory for promos (avoids scattered creation).
    if user_tier == "vip":
        promo = make_item({"type": "warranty", "months": 12, "price": 0.0})
    else:
        promo = make_item({"type": "apple", "variety": "Sample", "price": 1.0, "stock": 100})
    if promo is not None:
        cart.append(promo)

def compute_subtotal(cart):
    # Mixed responsibilities remain (money as float, ad hoc attributes).
    total = 0.0
    for item in cart:
        if hasattr(item, "price"):
            total += item.price
    return total

def apply_discounts(subtotal, cart, user_tier):
    # Delegates to strategy to avoid rigid if/elif chains and clarify stacking.
    return DISCOUNTS.calculate(subtotal, cart, user_tier)

def compute_tax(amount):
    return amount * TAX_RATE

def format_invoice(cart, subtotal, discount, tax, total):
    # Presentation still mixed with domain data shaping.
    lines = []
    lines.append("Invoice")
    for item in cart:
        name = getattr(item, "title", None) or getattr(item, "variety", None) or f"Warranty {getattr(item, 'months', '?')}m"
        price = getattr(item, "price", 0.0)
        lines.append(f"- {name}: {price:.2f}")
    lines.append(f"Subtotal: {subtotal:.2f}")
    lines.append(f"Discount: -{discount:.2f}")
    lines.append(f"Tax: {tax:.2f}")
    lines.append(f"Total: {total:.2f}")
    return "\n".join(lines)

def checkout(raw_items, user_tier):
    cart = load_cart(raw_items)
    add_promotional_item(cart, user_tier)
    subtotal = compute_subtotal(cart)
    discount = apply_discounts(subtotal, cart, user_tier)
    taxable = max(0.0, subtotal - discount)
    tax = compute_tax(taxable)
    total = taxable + tax
    return format_invoice(cart, subtotal, discount, tax, total)

if __name__ == "__main__":
    sample_items = [
        {"type": "book", "title": "Codex: Space Marines", "price": 399.90, "stock": 5},
        {"type": "digital_book", "title": "Rulebook (PDF)", "price": 199.90},
        {"type": "apple", "variety": "Squig Apple", "price": 9.90, "stock": 120},
    ]
    print(checkout(sample_items, user_tier="basic"))
