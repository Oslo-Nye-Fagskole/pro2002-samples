# legacy_shop_improved_factory.py -> Factory pattern improvement

from item_factory import Book, Apple, make_item

# Named constant replaces magic number; intent is explicit.
TAX_RATE = 0.25

# Item classes are removed from this file :)

def load_cart(raw_items):
    # Object creation centralized via factory (duplication removed; behavior unchanged).
    cart = []
    for it in raw_items:
        obj = make_item(it)
        if obj is not None:
            cart.append(obj)
        else:
            # Unknown type still silently ignored → fragile, hard to debug.
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
    # Mixed responsibilities remain: subtotal logic relies on ad hoc attributes across models.
    # Float accumulation for money remains.
    total = 0.0
    for item in cart:
        if hasattr(item, "price"):
            total += item.price
    return total


def apply_discounts(subtotal, cart, user_tier):
    # Rigid if/elif chain still mixes many rules (tier/cart-size/item/seasonal).
    # Order matters but is undocumented → unclear stacking behavior.
    # Multiple magic numbers remain in discount logic; also coupled to concrete classes via isinstance.
    discount = 0.0

    # tier-based
    if user_tier == "vip":
        discount += subtotal * 0.10

    # cart-size based
    if 500.0 < subtotal <= 1000.0:
        discount += subtotal * 0.05
    elif subtotal > 1000.0:
        discount += subtotal * 0.10

    # item-based
    has_apple = any(isinstance(x, Apple) for x in cart)
    if has_apple and user_tier != "vip":
        discount += 1.0  # small fixed discount if apples present

    # seasonal tweak (hard-coded)
    if any(isinstance(x, Book) and "Codex" in getattr(x, "title", "") for x in cart):
        discount += 15.0

    # Arbitrary cap adds more hidden stacking rules.
    return max(0.0, min(discount, subtotal * 0.5))


def compute_tax(amount):
    # No longer a magic number: uses TAX_RATE, semantics much clearer!
    return amount * TAX_RATE


def format_invoice(cart, subtotal, discount, tax, total):
    # Presentation still mixed with domain data shaping (name resolution, string building).
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
    # Orchestrates flow but still depends on remaining issues (discount rigidity, formatting mix).
    cart = load_cart(raw_items)
    add_promotional_item(cart, user_tier)

    subtotal = compute_subtotal(cart)
    discount = apply_discounts(subtotal, cart, user_tier)
    taxable = max(0.0, subtotal - discount)  # Assumes all items taxable.
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
