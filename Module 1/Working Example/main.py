# main.py

from logger import ConsoleLogger
from items import Book, DigitalBook, Apple, Warranty
from shop import Shop
from display import display

def run():
    logger = ConsoleLogger()

    shop = Shop([
        Book("Codex: Space Marines", 399.90, 5),
        DigitalBook("Warhammer 40k Rulebook (PDF)", 199.90),
        Apple("Squig Apple", 9.90, 120),
    ])
    shop.add(Warranty(24, 249.90))  # Extended warranty from the Mechanicus

    display(shop, logger)
    logger.log("Total price of all items: " + str(shop.total_price()))

if __name__ == "__main__":
    run()