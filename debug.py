from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("Creating customers...")
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    print("\nCreating coffees...")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    
    print("\nCreating orders...")
    order1 = alice.create_order(latte, 5.0)
    order2 = bob.create_order(latte, 7.0)
    order3 = alice.create_order(espresso, 6.0)
    
    print("\nDebug Information:")
    print("Customer Alice:")
    print(alice)
    print("Customer Bob:")
    print(bob)
    
    print("\nCoffee Latte:")
    print(latte)
    print(f"Number of Orders: {latte.num_orders()}")
    print(f"Average Price: {latte.average_price()}")
    
    print("\nCoffee Espresso:")
    print(espresso)
    print(f"Number of Orders: {espresso.num_orders()}")
    print(f"Average Price: {espresso.average_price()}")
    
    print("\nOrders:")
    print(order1)
    print(order2)
    print(order3)
    
    print("\nUnique coffees ordered by Alice:")
    print(alice.coffees())
    
    print("\nUnique customers who ordered Latte:")
    print(latte.customers())

#    example
    print("\nMost Aficionado for Latte:")
    print(Customer.most_aficionado(latte))

if __name__ == "__main__":
    main()
