import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):

    def setUp(self):
        # Clear all orders before each test
        Order._all_orders.clear()

    def test_name_setter_and_getter(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

        with self.assertRaises(TypeError):
            c.name = 123  # not a string

        with self.assertRaises(ValueError):
            c.name = ""  # too short

        with self.assertRaises(ValueError):
            c.name = "A" * 16  # too long

        c.name = "Bob"
        self.assertEqual(c.name, "Bob")

    def test_orders_and_coffees_relationship(self):
        c = Customer("Alice")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Mocha")

        # Initially, no orders or coffees
        self.assertEqual(c.orders(), [])
        self.assertEqual(c.coffees(), [])

        # Create orders
        order1 = c.create_order(coffee1, 4.5)
        order2 = c.create_order(coffee2, 5.0)
        order3 = c.create_order(coffee1, 3.5)

        self.assertEqual(len(c.orders()), 3)
        self.assertCountEqual(c.coffees(), [coffee1, coffee2])

    def test_create_order_validations(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")

        order = c.create_order(coffee, 7.0)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 7.0)

        with self.assertRaises(TypeError):
            c.create_order("not_coffee", 5.0)

        with self.assertRaises(ValueError):
            c.create_order(coffee, 0.5)  # price too low

    def test_most_aficionado(self):
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        coffee = Coffee("Latte")

        # No orders yet
        self.assertIsNone(Customer.most_aficionado(coffee))

        # Create orders
        c1.create_order(coffee, 4.0)
        c1.create_order(coffee, 3.0)
        c2.create_order(coffee, 8.0)

        self.assertEqual(Customer.most_aficionado(coffee), c2)

    def test_most_aficionado_no_orders(self):
        coffee = Coffee("Latte")
        self.assertIsNone(Customer.most_aficionado(coffee))

if __name__ == "__main__":
    unittest.main()
