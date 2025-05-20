import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    james = Customer("James")
    latte = Coffee("Latte")
    order = Order(james, latte, 5.0)

    assert order.customer == james
    assert order.coffee == latte
    assert order.price == 5.0

def test_order_price_validation():
    james = Customer("James")
    latte = Coffee("Latte")

    with pytest.raises(ValueError):
        Order(james, latte, 0)  

    with pytest.raises(ValueError):
        Order(james, latte, 11.0)  
