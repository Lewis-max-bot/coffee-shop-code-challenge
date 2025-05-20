import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):

    def setUp(self):
        Order._all_orders.clear()

    def test_name_immutable_and_validation(self):
        c = Coffee("Latte")
        self.assertEqual(c.name, "Latte")

        with self.assertRaises(AttributeError):
            c.name = "Espresso"  # should be immutable

        with self.assertRaises(TypeError):
            Coffee(123)  # name must be string

        with self.assertRaises(ValueError):
            Coffee("ab")  # less than 3 chars

    def test_orders_and_customers_relationship(self):
        coffee = Coffee("Mocha")
        c1 = Customer("Alice")
        c2 = Customer("Bob")

        # No orders initially
        self.assertEqual(coffee.orders(), [])
        self.assertEqual(coffee.customers(), [])

        # Create orders
        c1.create_order(coffee, 5.0)
        c2.create_order(coffee, 6.0)
        c1.create_order(coffee, 4.0)

        self.assertEqual(len(coffee.orders()), 3)
        self.assertCountEqual(coffee.customers(), [c1, c2])

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0)

        c = Customer("Alice")
        c.create_order(coffee, 3.5)
        c.create_order(coffee, 4.5)
        c.create_order(coffee, 5.0)

        self.assertEqual(coffee.num_orders(), 3)
        self.assertAlmostEqual(coffee.average_price(), (3.5 + 4.5 + 5.0) / 3)

if __name__ == "__main__":
    unittest.main()
