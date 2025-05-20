class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        # Validate customer and coffee types
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        # Validate price type and range
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        # Register this order globally
        Order._all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all_orders(cls):
        return cls._all_orders
