class Pizza:
    """Class for base pizza."""
    def __init__(self):
        self.price = 50.0
        self.tomato_sauce = 75

    def __iter__(self):
        for key, value in self.__dict__.items():
            i = str(key).find("__")
            if i != -1:
                key = str(key)[i + 2:]
            yield key, value

    def __str__(self):
        res = ""
        for ingr, weight in dict(self).items():
            if ingr != "price":
                res += ingr + ": " + str(weight) + "g\n"
        return res

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Price must be float")
        if price <= 0:
            raise ValueError("Price must be positive")
        self.__price = price

    @property
    def tomato_sauce(self):
        return self.__tomato_sauce

    @tomato_sauce.setter
    def tomato_sauce(self, tomato_sauce):
        if not isinstance(tomato_sauce, int):
            raise TypeError("Weigth of tomato sauce must be integer")
        if tomato_sauce <= 0:
            raise ValueError("Weight of tomato sauce must be positive")
        self.__tomato_sauce = tomato_sauce


class MondayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.price = 65.0
        self.ham = 50
        self.cheese = 100

    @property
    def ham(self):
        return self.__ham

    @ham.setter
    def ham(self, ham):
        if not isinstance(ham, int):
            raise TypeError("Weigth of ham must be integer")
        if ham <= 0:
            raise ValueError("Weight of ham must be positive")
        self.__ham = ham

    @property
    def cheese(self):
        return self.__cheese

    @cheese.setter
    def cheese(self, cheese):
        if not isinstance(cheese, int):
            raise TypeError("Weigth of cheese must be integer")
        if cheese <= 0:
            raise ValueError("Weight of cheese must be positive")
        self.__cheese = cheese


class TuesdayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.price = 80.0
        self.salami = 150
        self.cheese = 100

    @property
    def salami(self):
        return self.__salami

    @salami.setter
    def salami(self, salami):
        if not isinstance(salami, int):
            raise TypeError("Weigth of salami must be integer")
        if salami <= 0:
            raise ValueError("Weight of salami must be positive")
        self.__salami = salami

    @property
    def cheese(self):
        return self.__cheese

    @cheese.setter
    def cheese(self, cheese):
        if not isinstance(cheese, int):
            raise TypeError("Weigth of cheese must be integer")
        if cheese <= 0:
            raise ValueError("Weight of cheese must be positive")
        self.__cheese = cheese


class WednesdayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.price = 70.0
        self.tomato_sauce = 65
        self.chicken = 150
        self.tomatoes = 70

    @property
    def chicken(self):
        return self.__chicken

    @chicken.setter
    def chicken(self, chicken):
        if not isinstance(chicken, int):
            raise TypeError("Weigth of chicken must be integer")
        if chicken <= 0:
            raise ValueError("Weight of chicken must be positive")
        self.__chicken = chicken

    @property
    def tomatoes(self):
        return self.__tomatoes

    @tomatoes.setter
    def tomatoes(self, tomatoes):
        if not isinstance(tomatoes, int):
            raise TypeError("Weigth of tomatoes must be integer")
        if tomatoes <= 0:
            raise ValueError("Weight of tomatoes must be positive")
        self.__tomatoes = tomatoes


class ThursdayPizza(TuesdayPizza):
    def __init__(self):
        super().__init__()
        self.price = 85.0
        self.tomato_sauce = 60
        self.salami = 100
        self.cheese = 120
        self.tomatoes = 80

    @property
    def tomatoes(self):
        return self.__tomatoes

    @tomatoes.setter
    def tomatoes(self, tomatoes):
        if not isinstance(tomatoes, int):
            raise TypeError("Weigth of tomatoes must be integer")
        if tomatoes <= 0:
            raise ValueError("Weight of tomatoes must be positive")
        self.__tomatoes = tomatoes


class FridayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.price = 100.0
        self.tomato_sauce = 100
        self.salami = 70
        self.ham = 60
        self.chicken = 50

    @property
    def salami(self):
        return self.__salami

    @salami.setter
    def salami(self, salami):
        if not isinstance(salami, int):
            raise TypeError("Weigth of salami must be integer")
        if salami <= 0:
            raise ValueError("Weight of salami must be positive")
        self.__salami = salami

    @property
    def ham(self):
        return self.__ham

    @ham.setter
    def ham(self, ham):
        if not isinstance(ham, int):
            raise TypeError("Weigth of ham must be integer")
        if ham <= 0:
            raise ValueError("Weight of ham must be positive")
        self.__ham = ham

    @property
    def chicken(self):
        return self.__chicken

    @chicken.setter
    def chicken(self, chicken):
        if not isinstance(chicken, int):
            raise TypeError("Weigth of chicken must be integer")
        if chicken <= 0:
            raise ValueError("Weight of chicken must be positive")
        self.__chicken = chicken


class SaturdayPizza(WednesdayPizza):
    def __init__(self):
        super().__init__()
        self.price = 80.0
        self. cheese = 100

    @property
    def cheese(self):
        return self.__cheese

    @cheese.setter
    def cheese(self, cheese):
        if not isinstance(cheese, int):
            raise TypeError("Weigth of cheese must be integer")
        if cheese <= 0:
            raise ValueError("Weight of cheese must be positive")
        self.__cheese = cheese


class SundayPizza(FridayPizza):
    def __init__(self):
        super().__init__()
        self.price = 100.0
        self.salami = 50
        self.ham = 50
        self.cheese = 100

    @property
    def cheese(self):
        return self.__cheese

    @cheese.setter
    def cheese(self, cheese):
        if not isinstance(cheese, int):
            raise TypeError("Weigth of cheese must be integer")
        if cheese <= 0:
            raise ValueError("Weight of cheese must be positive")
        self.__cheese = cheese
