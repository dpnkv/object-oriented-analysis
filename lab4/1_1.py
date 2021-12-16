import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be integer")
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be integer")
        if not denominator:
            raise ZeroDivisionError("Denominator equals to zero")

        gcd = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be integer")
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be integer")
        if not denominator:
            raise ZeroDivisionError("Denominator equals to zero")
        self.__denominator = denominator

    def get_float(self):
        return self.numerator / self.denominator

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __add__(self, other):
        if isinstance(other, Rational):
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Rational(numerator, denominator)
        if isinstance(other, int):
            numerator = other * self.denominator + self.numerator
            return Rational(numerator, self.denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return Rational(numerator, denominator)
        if isinstance(other, int):
            numerator = self.numerator - other * self.denominator
            return Rational(numerator, self.denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        if isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
        elif isinstance(other, int):
            self.numerator += other * self.denominator

        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        return self

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator *= other.denominator
        elif isinstance(other, int):
            self.numerator -= other * self.denominator

        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        return self

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
        if isinstance(other, int):
            self.numerator *= other

        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        return self

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.denominator
            self.denominator *= other.numerator
        if isinstance(other, int):
            self.denominator *= other

        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        return self

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator < other * self.denominator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator > other * self.denominator
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator <= other * self.denominator
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator >= other * self.denominator
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator, self.denominator) == (other.numerator, other.denominator)
        if isinstance(other, int):
            return self.numerator == other * self.denominator
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Rational):
            return (self.numerator, self.denominator) != (other.numerator, other.denominator)
        if isinstance(other, int):
            return self.numerator != other * self.denominator
        return NotImplemented


if __name__ == "__main__":
    r1 = Rational(23, 7)
    r2 = Rational(52, 3)

    print(f"r1: {r1}; {r1.get_float():.2f}")
    print(f"r2: {r2}; {r2.get_float():.2f}\n")
    print(f"r2 + 3 = {r2 + 3}")
    print(f"r1 * 2 = {r1 * 2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 <= r2: {r1 < r2}")
    print(f"r2 == 16: {r2 == 16}")
