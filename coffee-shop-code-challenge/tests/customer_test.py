
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    james = Customer("James")
    assert james.name == "James"

with pytest.raises(ValueError):
    Customer("")  
