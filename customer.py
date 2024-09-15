class Customer:
    def __init__(self, name):#initialise the Customer instance
        self.name = name
        self._orders = []

#define a property to access the customer's name
    @property
    def name(self):
        return self._name

#defining a setter for the customer's name
    @name.setter
    def name(self, value):
        self._name = value
        self._validate_name()


# private method to validate the customer's name
    def _validate_name(self):
        # check if name is a string and its length is between 1 and 15
        if not isinstance(self._name, str) or not (1 <= len(self._name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")


# return the list of orders for this customer
    def orders(self):
        return self._orders


# method to get a list of unique coffeees from the customer's ordrs
    def coffees(self):
        return list({order.coffee for order in self._orders})


# method to create a new order and add it to the Customer's orders    
    def create_order(self, coffee, price):
        order = order(self, coffee, price)
        self._orders.append(order)
        return order
    

#defining the representation of the Customer instance as a string
    def __str__(self):
        return f"Customer(name={self.name}, orders={len(self._orders)}, coffees={self.coffees()})"
    

customer1 = Customer("Owiti")#instantiate customer with the name "Owiti"
print(customer1)