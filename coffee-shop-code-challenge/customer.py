class Customer:
    def __init__(self, name):
        self.name = name  # uses setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("name length must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        # return list of all orders for this customer
        return [order for order in Order.all_orders() if order.customer == self]

    def coffees(self):
        # return unique list of coffees ordered by this customer
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        # create a new Order linked to this customer and coffee
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Find customer who spent the most on the given coffee
        orders = [order for order in Order.all_orders() if order.coffee == coffee]
        if not orders:
            return None

        # Calculate spending per customer
        spending = {}
        for order in orders:
            spending[order.customer] = spending.get(order.customer, 0) + order.price

        # Return the customer with max spending
        return max(spending, key=spending.get)
