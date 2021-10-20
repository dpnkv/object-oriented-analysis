class Product:
    """A class that represents a product."""
    def __init__(self, price, description="", weigth=0):
        if not isinstance(price, float):
            raise TypeError("Price must be float")
        if price < 0:
            raise ValueError("Price must be non-negative")

        if not isinstance(weigth, float):
            raise TypeError("Weigth must be float")
        if weigth < 0:
            raise ValueError("Weigth must be non-negative")

        self.__price = price
        self.__description = description
        self.__weigth = weigth

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Price must be float")
        if price < 0:
            raise ValueError("Price must be non-negative")
        self.__price = price

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be string")
        self.__description = description

    @property
    def weigth(self):
        return self.__weigth

    @weigth.setter
    def weigth(self, weigth):
        if not isinstance(weigth, float):
            raise TypeError("Weigth must be float")
        if weigth < 0:
            raise ValueError("Weigth must be non-negative")
        self.__weigth = weigth


class Customer:
    """A class that represents a customer."""
    def __init__(self, name, surname):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Name and surname must be strings")
        if not name:
            raise ValueError("Name must not be empty")
        if not surname:
            raise ValueError("Surname must not be empty")

        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must be string")
        self.__surname = surname

class Order:
    """A class that represents an order."""
    def __init__(self, customer=None, *products):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer object")
        if not all(isinstance(product, Product) for product in products):
            raise TypeError("Products must be Product object")

        self.__customer = customer
        self.__products = products
           
    def get_total_price(self):
        """Return total price of order."""
        self.__total_price = 0
        for product in self.__products:
            self.__total_price += product.price
        return self.__total_price

    @property
    def customer(self):
        return self.__customer


bread = Product(15.5, "Just a bread", 0.5)
butter = Product(30.1, "A normal butter", 0.4)
bread.price = 13.2
print(bread.price)
print(bread.description)

jack = Customer("Jack", "Hallnigan")

order = Order(jack, bread, butter)
print(order.get_total_price())
print(f"Customer: {order.customer.name} {order.customer.surname}")
