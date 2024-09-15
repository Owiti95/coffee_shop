import pytest
from coffee import Coffee
from order import Order
from customer import Customer

def test_coffee_initialization():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    assert coffee.orders() == []

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("")

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Owiti")
    order = Order(customer, coffee, 7.5)
    
    coffee._orders.append(order)
    
    assert len(coffee.orders()) == 1
    assert order in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("Owiti")
    customer2 = Customer("Alice")
    
    customer1.create_order(coffee, 7.5)
    customer2.create_order(coffee, 5.0)
    
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_coffee_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("Owiti")
    customer.create_order(coffee, 7.5)
    
    assert coffee.num_orders() == 1

def test_coffee_average_price():
    coffee = Coffee("Latte")
    customer = Customer("Owiti")
    customer
