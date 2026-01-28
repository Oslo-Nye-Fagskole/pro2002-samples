class OrderProcessor:
    def create_order(self, order_type):
        if order_type == "online":
            return OnlineOrder()
        elif order_type == "store":
            return StoreOrder()
        elif order_type == "phone":
            return PhoneOrder()
        else:
            raise ValueError("Unknown order type")

class OnlineOrder:
    pass

class StoreOrder:
    pass

class PhoneOrder:
    pass