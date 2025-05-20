class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self.name = name
        self._orders = []  

def place_order(self, coffee, price):
    order = order(self, coffee, price)
    self._orders.append(order)
    return order

def orders(self):
    return self._orders

def coffees(self):
    return list(set([order.coffee for order in self._orders]))  