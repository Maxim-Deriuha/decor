class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity + v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        self.capacity += v


# issubclass()
# isinstance()
# mro()
print(MoneyBox.mro())
