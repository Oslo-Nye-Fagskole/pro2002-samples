# discounts_strategy.py

class DiscountStrategy:
    # Strategy interface: returns discount amount for given context.
    def calculate(self, subtotal, cart, user_tier):
        return 0.0


class TierDiscount(DiscountStrategy):
    # Replaces: if user_tier == "vip": discount += subtotal * 0.10
    RATE_VIP = 0.10
    def calculate(self, subtotal, cart, user_tier):
        return subtotal * self.RATE_VIP if user_tier == "vip" else 0.0


class CartSizeDiscount(DiscountStrategy):
    # Replaces: cart-size thresholds (0.05/0.10 for >500 and >1000)
    THRESHOLD_LOW = 500.0
    THRESHOLD_HIGH = 1000.0
    RATE_LOW = 0.05
    RATE_HIGH = 0.10
    def calculate(self, subtotal, cart, user_tier):
        if self.THRESHOLD_LOW < subtotal <= self.THRESHOLD_HIGH:
            return subtotal * self.RATE_LOW
        if subtotal > self.THRESHOLD_HIGH:
            return subtotal * self.RATE_HIGH
        return 0.0


class ApplePresenceDiscount(DiscountStrategy):
    # Replaces: if has apple and not vip: +1.0
    FIXED = 1.0
    def calculate(self, subtotal, cart, user_tier):
        has_apple = any(type(x).__name__ == "Apple" for x in cart)
        return self.FIXED if has_apple and user_tier != "vip" else 0.0


class SeasonalCodexDiscount(DiscountStrategy):
    # Replaces: if any Book with "Codex" in title: +15.0
    FIXED = 15.0
    def calculate(self, subtotal, cart, user_tier):
        for x in cart:
            if type(x).__name__ == "Book" and "Codex" in getattr(x, "title", ""):
                return self.FIXED
        return 0.0


class CapStrategy(DiscountStrategy):
    # Replaces the 50% cap on total discount.
    CAP_RATE = 0.5
    def cap(self, subtotal, accumulated):
        return max(0.0, min(accumulated, subtotal * self.CAP_RATE))


class CompositeDiscountStrategy(DiscountStrategy):
    # Orchestrates stacking + final cap; preserves original stacking behavior.
    def __init__(self, strategies, cap_strategy=None):
        self.strategies = strategies
        self.cap_strategy = cap_strategy or CapStrategy()

    def calculate(self, subtotal, cart, user_tier):
        total = 0.0
        for s in self.strategies:
            total += s.calculate(subtotal, cart, user_tier)
        return self.cap_strategy.cap(subtotal, total)


def default_discount_strategy():
    # Behavior-preserving composition mirroring the legacy rules and order.
    return CompositeDiscountStrategy([
        TierDiscount(),
        CartSizeDiscount(),
        ApplePresenceDiscount(),
        SeasonalCodexDiscount(),
    ], cap_strategy=CapStrategy())
