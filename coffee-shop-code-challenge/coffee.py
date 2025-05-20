class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self.name = name
        self._orders = []  

def add_order(self, order):
    self._orders.append(order)

def orders(self):
    return self._orders

def customers(self):
    return list(set([order.customer for order in self._orders]))  

def num_orders(self):
    return len(self._orders)

def average_price(self):
    total_price = sum(order.price for order in self._orders)
    return total_price / len(self._orders) if self._orders else 0