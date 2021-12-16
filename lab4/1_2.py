class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Price must be float")
        if price < 0.0:
            raise ValueError("Price cannot be less than zero")
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be less than zero")
        self.__quantity = quantity

    def __add__(self, other):
        if isinstance(other, int):
            return Product(self.name, self.price, self.quantity + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Product(self.name, self.price, self.quantity - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Product(self.name, self.price * other, self.quantity)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if not other:
                raise ZeroDivisionError("Dividing by zero")
            return Product(self.name, self.price / other, self.quantity)
        return NotImplemented

    def __str__(self):
        return f"{self.name}: {self.quantity} pcs, {self.price} usd"


class Composition:
    def __init__(self, *products):
        self.products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if not all(isinstance(product, Product) for product in products):
            raise TypeError("Products must be Product type")
        self.__products = list(products)

    def __str__(self):
        res = ""
        for p in self.products:
            res += str(p) + '\n'
        return res

    def __iadd__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        self.products.append(other)
        return self

    def __isub__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        self.products.remove(other)
        return self

    def report_by_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty string")
        for p in self.products:
            if p.name == name:
                return str(p)


if __name__ == "__main__":
    p1 = Product("First", 100.3, 30)
    p2 = Product("Second", 50.0, 10)
    p3 = Product("Third", 90.1, 500)

    comp = Composition(p1, p2)
    print(comp)
    comp += p3
    print(comp)
    print(comp.report_by_name("Second"))
