import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from coffee import Coffee

def test_coffee_name():
    latte = Coffee("Latte")
    assert latte.name == "Latte"

with pytest.raises(ValueError):
    Coffee("T")  