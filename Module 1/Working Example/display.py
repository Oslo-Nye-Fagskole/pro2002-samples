# display.py

from contracts import Priceable, StockTrackable, LabelPrintable
from logger import Logger

def display_item(item, logger):
    if isinstance(logger, Logger):
        if isinstance(item, LabelPrintable):
            logger.log("Item: " + item.print_label())
        if isinstance(item, Priceable):
            logger.log("Price: " + str(item.get_price()))
        if isinstance(item, StockTrackable):
            logger.log("In stock: " + str(item.in_stock()))
        logger.log("")

def display(shop, logger):
    logger.log("Welcome! Items registered: " + str(len(shop)) + "\n")
    for item in shop:
        display_item(item, logger)