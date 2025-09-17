# What is this "Converter" converting?!?
class Converter:
    def __init__(self, factor, offset):
        self.factor = factor
        self.offset = offset

    def convert(self, value):
        return value * self.factor + self.offset


# Why such oddly specific numbers?!?
# And why "5/9" twice?!?
c = Converter(5/9, -32 * 5/9)
print(c.convert(212))