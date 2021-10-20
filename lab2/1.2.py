import math

class Rational:
    """Class that represents a rational number."""
    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator

        gcd = math.gcd(self.__numerator, self.__denominator)
        if denominator:
            self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def print_fraction(self):
        """Print number as a fraction."""
        print(str(self.__numerator) + '/' + str(self.__denominator))

    def print_float(self):
        """Print number as float number."""
        try:
            print(f"{self.__numerator / self.__denominator:.3f}")
        except ZeroDivisionError:
            print("Division by zero")

fraction = Rational(23, 7)
fraction.print_fraction()
fraction.print_float()
