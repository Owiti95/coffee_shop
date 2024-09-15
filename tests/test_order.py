import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_customer_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order("invalid_customer", coffee, 5.0)

def test_order_coffee_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, "invalid_coffee", 5.0)

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, -1.0)  # Invalid price
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # Invalid price

def test_order_price_property():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order.price == 5.0
    
    order.price = 7.5
    assert order.price == 7.5
    
    with pytest.raises(ValueError):
        order.price = 15.0  # Invalid price

def test_order_str_method():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert str(order) == "Order(customer=Alice, coffee=Latte, price=5.00)"
