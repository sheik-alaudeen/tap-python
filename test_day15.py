import pytest
def add_numbers(a, b):
    return a + b
def is_valid_customer_id(customer_id):
    return customer_id is not None and customer_id != ""
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def test_add_numbers():
    assert add_numbers(2, 3) == 5
def test_valid_customer_id():
    assert is_valid_customer_id("C001") == True
def test_invalid_customer_id():
    assert is_valid_customer_id(None) == False
def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)