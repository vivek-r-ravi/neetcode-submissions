class StoreItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


chips = StoreItem("Chips", 1.99)

print(chips.name)
print(chips.price)