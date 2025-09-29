def apply_discount_to_cart(cart):
    # Calculate total price of items in the cart
    total = sum(item.price_cents * item.qty for item in cart.items)

    # Critical business rule duplicated here:
    # 10% discount applied if total is above 50 NOK
    if total > 5000:
        total = int(total * 0.9)

    return total


def generate_invoice(order):
    # Format invoice header and customer info
    invoice = f"Invoice for order {order.id}\nCustomer: {order.user_email}\n"

    # Calculate total price of items in the order
    total = sum(item.price_cents * item.qty for item in order.items)

    # Same discount rule duplicated again:
    # Appears here in addition to the cart logic above
    # What happens if we decide to change the logic here; say give discounts to orders above a lesser total?
    if total > 5000:
        total = int(total * 0.9)

    invoice += f"Total (after discount if applicable): {total} cents"
    return invoice
