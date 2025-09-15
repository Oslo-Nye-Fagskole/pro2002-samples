# Data access layer: responsible only for storing and retrieving items
class ItemRepository:
    def __init__(self):
        self._items = []  # internal storage

    def add_item(self, item):
        self._items.append(item)

    def get_all(self):
        return self._items


# Business logic layer: applies rules and calculations, uses the repository
class ShopService:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def add_item(self, name, price):
        # business rule: create item and pass it to the repository
        self.repo.add_item({"name": name, "price": price})

    def get_items(self):
        # return all items through the service (hides repository details)
        return self.repo.get_all()

    def total_price(self):
        # calculate total value of all items
        return sum(item["price"] for item in self.repo.get_all())


# Presentation layer: interacts with the user and calls the service
class ShopUI:
    def __init__(self, service: ShopService):
        self.service = service

    def run(self):
        # add some example items
        self.service.add_item("Codex: Orks", 299)
        self.service.add_item("Squig Apple", 12.5)

        # display items
        print("Items in shop:")
        for item in self.service.get_items():
            print("-", item["name"], ":", item["price"], "kr")

        # display total price
        print("Total:", self.service.total_price(), "kr")


# Wiring the layers together
repo = ItemRepository()
service = ShopService(repo)
ui = ShopUI(service)

ui.run()