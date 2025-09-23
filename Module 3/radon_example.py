# High CC and potential low MI; Radon should flag these as refactor candidates.

def calculate_order_total(items, user_tier, order_type, coupons):
    total = 0
    for it in items:
        if it is None or getattr(it, "qty", 0) <= 0:
            continue
        price = getattr(it, "price_cents", 0)

        # branching by category and quantity (adds to CC)
        if getattr(it, "category", "") == "fragile" and it.qty > 3:
            price = int(price * 0.95)
        elif getattr(it, "category", "") == "clearance":
            if it.qty > 10:
                price = int(price * 0.8)
            else:
                price = int(price * 0.9)

        # branching by tier and order type (adds to CC)
        if user_tier == "gold":
            price = int(price * 0.9)
        elif user_tier == "silver":
            if order_type == "express":
                price = int(price * 0.97)
            else:
                price = int(price * 0.95)
        elif user_tier == "bronze":
            if order_type != "economy":
                price = int(price * 0.99)

        total += price * it.qty

    # nested discount logic (adds to CC, may lower MI)
    if total > 5000:
        if "WELCOME10" in coupons:
            total = int(total * 0.9)
        elif "FREESHIP" in coupons and order_type != "express":
            pass
        else:
            if user_tier != "bronze":
                total -= 200
            else:
                total -= 100

    return total


# Intentional duplication below (dashboards can detect duplication; Radon shows CC per function)

def estimate_shipping_cost(weight, speed):
    cost = 0
    if speed == "express":
        if weight < 1000:
            cost = 149
        elif weight < 5000:
            cost = 299
        else:
            cost = 499
    else:
        if weight < 1000:
            cost = 49
        elif weight < 5000:
            cost = 99
        else:
            cost = 199
    return cost


def estimate_delivery_cost(weight, speed):  # duplicate structure/thresholds
    cost = 0
    if speed == "express":
        if weight < 1000:
            cost = 149
        elif weight < 5000:
            cost = 299
        else:
            cost = 499
    else:
        if weight < 1000:
            cost = 49
        elif weight < 5000:
            cost = 99
        else:
            cost = 199
    return cost