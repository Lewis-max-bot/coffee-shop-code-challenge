class Order:
    all_orders = []  

    def __init__(self, customer, coffee, price):
       if not (1.0 <= price <= 10.0):
          raise ValueError("Price must be between 1.0 and 10.0.")
       self.customer = customer
       self.coffee = coffee
       self.price = price
       Order.all_orders.append(self)
       coffee.add_order(self)  

    @classmethod
    def all(cls):
       return cls.all_orders