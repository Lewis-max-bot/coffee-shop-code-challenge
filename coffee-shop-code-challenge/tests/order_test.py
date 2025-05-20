import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):

    def setUp(self):
        Order._all_orders.clear()

    def test_order_init_validations(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")

        # Valid order
        o = Order(c, coffee, 5.5)
        self.assertEqual(o.customer, c)
        self.assertEqual(o.coffee, coffee)
        self.assertEqual(o.price, 5.5)

        # Invalid customer type
        with self.assertRaises(TypeError):
            Order("not_customer", coffee, 5.0)

        # Invalid coffee type
        with self.assertRaises(TypeError):
            Order(c, "not_coffee", 5.0)

        # Invalid price type
        with self.assertRaises(TypeError):
            Order(c, coffee, "5.0")

        # Price out of range
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(c, coffee, 15)

    def test_price_immutable(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        o = Order(c, coffee, 6.0)

        with self.assertRaises(AttributeError):
            o.price = 7.0

    def test_order_registration(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")

        self.assertEqual(len(Order.all_orders()), 0)
        o = Order(c, coffee, 5.0)
        self.assertEqual(len(Order.all_orders()), 1)
        self.assertIn(o, Order.all_orders())

if __name__ == "__main__":
    unittest.main()
