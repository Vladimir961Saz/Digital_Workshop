# №1
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение a должно быть числом (int или float)")
        if value <= 0:
            raise ValueError("Значение a должно быть положительным")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение b должно быть числом (int или float)")
        if value <= 0:
            raise ValueError("Значение b должно быть положительным")
        self._b = value

    @property
    def area(self):
        # Площадь прямоугольника
        return self.a * self.b

    @property
    def perimeter(self):
        # Периметр прямоугольника
        return 2 * (self.a + self.b)


rect = Rectangle(3, 4)
print(rect.area)
print(rect.perimeter)
rect.a = 5.5
try:
    rect.b = -10
except ValueError as e:
    print(e)

# №2
class ComplexNumber:
    def __init__(self, real, imag):
        if not isinstance(real, (int, float)) or not isinstance(imag, (int, float)):
            raise TypeError(
                "Аргументы real и imag должны быть числами (int или float).")

        self._real = real
        self._imag = imag

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Складывать можно только с другим ComplexNumber.")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(4, 6)
c3 = c1 + c2
print(c3)

try:
    c4 = c1 + 3
except TypeError as e:
    print(e)

try:
    c5 = 3 + c1
except TypeError as e:
    print(e)
