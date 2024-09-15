#importing customer and coffee classes
from customer import Customer
from coffee import Coffee


class Order:
#  initialize an order instance with a customer, coffee and price
    def __init__(self, customer, coffee, price):
        self.customer = customer  
        self.coffee = coffee      
        self.price = price


# property to access the price of the order
    @property
    def price(self):
        return self._price
    

# a setter for the price of the order
    @price.setter
    def price(self, value):
        self._price = value
        self._validate_price()


# property to access the customer associated with the order
    @property
    def customer(self):
        return self._customer
    

# setter for the customer of the order
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer class.")
        self._customer = value


# a property for the coffee associated with the order
    @property
    def coffee(self):
        return self._coffee
    

# a setter for the coffee of the order
    @coffee.setter
    def coffee(self, value):
        #ensuring that the coffee is an instance of the Coffee class
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee class.")
        self._coffee = value


#private method to validate the price of the order
    def _validate_price(self):
#check if the price is a number between 1 and 10
        if not isinstance(self._price, (int, float)) or not (1.0 <= self._price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0.")


# defining how to represent the order instance as a string
    def __str__(self):
        #return a string representation of the order including customer name, coffee name, and price
        return (f"Order(customer={self.customer.name}, coffee={self.coffee.name}, "
                f"price={self.price:.2f})")
    

if __name__ == "__main__":
    customer = Customer("Owiti")#customer instance
    coffee = Coffee("Latte")#coffee instance
    order = Order(customer, coffee, 7.5)#order instance
    print(order)