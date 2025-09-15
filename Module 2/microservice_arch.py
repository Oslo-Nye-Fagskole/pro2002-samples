# Product service: responsible only for providing product information
class ProductService:
    def get_products(self):
        return ["Codex: Orks", "Squig Apple"]


# Order service: responsible only for handling orders
class OrderService:
    def __init__(self):
        self.orders = []  # keeps a record of placed orders

    def place_order(self, product):
        self.orders.append(product)
        print("Order placed for:", product)


# Simulate communication between independent services
product_service = ProductService()
order_service = OrderService()

# Client asks product service for available products
products = product_service.get_products()
print("Available products:", products)

# Client asks order service to place an order
order_service.place_order(products[0])