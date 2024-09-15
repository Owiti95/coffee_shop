Coffee shop system
This project models a simple coffee shop domain. It defines three classes: Customer, Coffee, and Order, and establishes relationships between them:

A Customer can make many Orders.
Coffee can have many Orders.
An Order belongs to both a Customer and a Coffee.
The project demonstrates:
Class relationships
Instance Methods
Class Methods
Prerequisites
Python3
Text editor eg vs code
SET-UP
Clone the repository to your local machine: git@github.com:kiprotichabiud/phase-3-challenge-2.git
Navigate to the project directory: cd coffee-shop
Structure
Customer. py:
Defines the Customer class.
Contains methods to create customers, retrieve orders, retrieve coffees, and create new orders.
Ensures that customer names are validated and are within the required length.
Coffee. py:
Defines the Coffee class.
Contains methods to manage coffee orders and retrieve a list of customers who have ordered a particular coffee.
Also includes aggregate methods like num_orders (total number of orders for the coffee) and average_price (average price for a coffee).
Order. py:
Defines the Order class.
Manages the creation of an order that links a customer, a coffee, and the price for the order.
Ensures that prices are validated and within the allowed range.
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch: git checkout -b my-feature-branch
Make your changes and commit them: git commit -m 'Add some feature'
Push to the branch: git push origin - - my-feature-branch
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

AUTHOR
Hannington Owiti