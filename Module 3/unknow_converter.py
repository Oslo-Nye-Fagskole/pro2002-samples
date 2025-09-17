class Converter:
    def __init__(self, factor, offset):
        self.factor = factor
        self.offset = offset

    def convert(self, value):
        return value * self.factor + self.offset


# What is this "Converter" converting?!?
c = Converter(5/9, -32 * 5/9)
print(c.convert(212))