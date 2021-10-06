class Rectangle:
    def __init__(self):
        self.__length = 1
        self.__width = 1

    def set_length(self, length):
        if isinstance(length, float) and 0.0 < length < 20.0:
            self.__length = length
        else:
            raise ValueError("Length must be float and in range from 0.0 to 20.0")

    def set_width(self, width):
        if isinstance(width, float) and 0.0 < width < 20.0:
            self.__width = width
        else:
            raise ValueError("Width must be float and in range from 0.0 to 20.0")

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width
    
    def get_perimeter(self):
        return (self.__length + self.__width) * 2
        
    def get_area(self):
        return self.__length * self.__width


rect = Rectangle()
rect.set_length(2.0)
rect.set_width(6.0)
print("Length: " + str(rect.get_length()))
print("Width: " + str(rect.get_width()))
print("Perimeter: " + str(rect.get_perimeter()))
print("Area: " + str(rect.get_area()))
