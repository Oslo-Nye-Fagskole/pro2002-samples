# legacy_shop.py

# Item classes live in same file as business logic: mixes responsibilities.
class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock


class DigitalBook:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Apple:
    def __init__(self, variety, price, stock):
        self.variety = variety
        self.price = price
        self.stock = stock


class Warranty:
    def __init__(self, months, price):
        self.months = months
        self.price = price


def load_cart(raw_items):
    # Scattered object creation (duplicated elsewhere). Adding a new type means editing here.
    cart = []
    for it in raw_items:
        t = it.get("type")
        if t == "book":
            cart.append(Book(it["title"], it["price"], it.get("stock", 0)))
        elif t == "digital_book":
            cart.append(DigitalBook(it["title"], it["price"]))
        elif t == "apple":
            cart.append(Apple(it["variety"], it["price"], it.get("stock", 0)))
        elif t == "warranty":
            cart.append(Warranty(it["months"], it["price"]))
        else:
            # Unknown type silently ignored: fragile, hard to debug.
            pass
    return cart


def add_promotional_item(cart, user_tier):
    # Duplicates creation logic again (should be centralized).
    if user_tier == "vip":
        cart.append(Warranty(12, 0.0))
    else:
        cart.append(Apple("Sample", 1.0, 100))


def compute_subtotal(cart):
    # Mixed responsibilities: subtotal logic relies on ad hoc attributes across models.
    total = 0.0
    for item in cart:
        if hasattr(item, "price"):
            total += item.price
    return total


def apply_discounts(subtotal, cart, user_tier):
    # Rigid if/elif chain mixes many rules together (tier/cart-size/item/seasonal).
    # Order matters but is undocumented: unclear stacking behavior.
    # Multiple occurrences of magic numbers for the various discounts.
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
        discount += 1.0

    # seasonal tweak (hard-coded content check)
    if any(isinstance(x, Book) and "Codex" in x.title for x in cart):
        discount += 15.0

    # Arbitrary cap adds more hidden stacking rules.
    return max(0.0, min(discount, subtotal * 0.5))


def compute_tax(amount):
    return amount * 0.25  # magic number, unclear what it represents


def format_invoice(cart, subtotal, discount, tax, total):
    # Presentation mixed with domain data shaping (name resolution, string building).
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
    # Orchestrates flow but depends on the issues above (creation, discounts, formatting).
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
