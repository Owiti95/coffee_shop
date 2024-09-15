# defining the coffee class
class Coffee:
    def __init__(self, name): # initialising a coffee instance with a name attribute
        self.name = name  # set the coffee's name using the property setter
        self._orders = [] # initialize an empty list to store orders

    #defining a property for the coffee's name
    @property
    def name(self):
        return self._name # return the private variable_name

   
    @name.setter # define the setter for the coffee's name
    def name(self, value):
        self._name = value # set the private variable_name
        self._validate_name() # validate the name to ensure it's correct


    def _validate_name(self): # private method to validate the coffee's name
        # check if the name is a string and has atleast 3 character
        if not isinstance(self._name, str) or len(self._name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")# raise an error


    # method to get the list of orders
    def orders(self): 
        return self._orders # returning order list


    # method that gets the list of unique customers
    def customers(self):
        # set comprehension that gets unique customers from the orders 
        return list({order.customer for order in self._orders})


    def num_orders(self):# method that gets the number of orders
        return len(self._orders) # return the number of orders

    
    def average_price(self): # method that calculates the average price of orders
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders) # the sum of all prices
        return total_price / len(self._orders) # returning average price

    def __str__(self): # defining how to represent the coffee instance as a string
        return f"Coffee(name={self.name})" # returning the string representation of coffee
    

if __name__ == "__main__":
    coffee1 = Coffee("Latte") # create a "cappuchino" coffee instance
    # print the coffee instance which uses the __str__method
    print(coffee1)
