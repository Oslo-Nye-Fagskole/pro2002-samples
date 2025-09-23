# Missing module docstring (C0114)

import sys  # unused import (W0611)

def calculate_price(price, qty, tax_rate=0.25, discount=0.1):  # missing function docstring (C0116)
    total = price * qty
    if total > 1000:
        total = total - (total * discount)  # discount logic could be refactored (R0916)
    return total

def process_items(items=[]):  # dangerous mutable default argument (W0102)
    for i in items:
        print("Processing:", i)

def SummonTheEmperor():  # invalid function name style (C0103)
    holyBolter = 42  # variable name doesn’t follow snake_case (C0103)
    return holyBolter