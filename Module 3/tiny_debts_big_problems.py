# "Magic number"
# The business tax rate of 0.22 (backbone of the Norwegian bureaucracy) is hidden directly in the code.
# No explanation of where it comes from or where else relevant.
def calculate_business_tax(profit):
    return profit * 0.22


# Duplicated logic: two functions with identical formulas for calculating shipping cost.
# The only difference is the fixed fee, but the rest of the logic is repeated.
def shipping_domestic(weight):
    return weight * 5 + 10

def shipping_international(weight):
    return weight * 5 + 30


# Poor naming: the function and variable names offer no clue to the intent.
# No one, let alone a new developer cannot tell what this is calculating.
# Most likely, the person who wrote this will also have forgotten after a while...
def do_it(x):
    return x * (x - 1) / 2
