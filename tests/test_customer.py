import pytest
from customer import Customer
from order import Order
from coffee import Coffee

def test_customer_initialization():
    customer = Customer("Owiti")
    assert customer.name == "Owiti"
    assert customer.orders() == []

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_create_order():
    customer = Customer("Owiti")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 7.5)
    
    assert len(customer.orders()) == 1
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 7.5

def test_customer_coffees():
    customer = Customer("Owiti")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 7.5)
    customer.create_order(coffee2, 5.0)
    
    coffees = customer.coffees()
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees

def test_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Latte")
    
    customer1.create_order(coffee, 7.5)
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    
    assert customer1.most_aficionado(coffee) == customer1
    assert customer2.most_aficionado(coffee) == customer1
