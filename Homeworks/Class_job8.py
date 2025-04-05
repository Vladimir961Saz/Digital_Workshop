from math import gcd

class Fraction:
    _cache = {}

    def __new__(cls, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        common_divisor = gcd(numerator, denominator)
        numerator = (numerator // common_divisor) * (-1 if denominator < 0 else 1)
        denominator = abs(denominator // common_divisor)
        key = (numerator, denominator)
        if key in cls._cache:
            return cls._cache[key]
        instance = super().__new__(cls)
        cls._cache[key] = instance
        return instance

    def __init__(self, numerator: int, denominator: int):
        if hasattr(self, '_initialized'):
            return
        self._numerator, self._denominator = numerator, denominator
        self._initialized = True

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def _operate(self, other: "Fraction", op) -> "Fraction":
        return Fraction(op(self._numerator * other._denominator, other._numerator * self._denominator),
                        self._denominator * other._denominator)

    def __add__(self, other: "Fraction") -> "Fraction":
        return self._operate(other, lambda x, y: x + y)

    def __sub__(self, other: "Fraction") -> "Fraction":
        return self._operate(other, lambda x, y: x - y)

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction(self._numerator * other._numerator, self._denominator * other._denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        if other._numerator == 0:
            raise ZeroDivisionError("Нельзя делить на дробь с нулевым числителем")
        return Fraction(self._numerator * other._denominator, self._denominator * other._numerator)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Fraction) and self._numerator == other._numerator and self._denominator == other._denominator

    def __lt__(self, other: "Fraction") -> bool:
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __le__(self, other: "Fraction") -> bool:
        return self < other or self == other

    def __gt__(self, other: "Fraction") -> bool:
        return not (self <= other)

    def __ge__(self, other: "Fraction") -> bool:
        return not (self < other)

    def __hash__(self) -> int:
        return hash((self._numerator, self._denominator))

    @property
    def value(self) -> float:
        return round(self._numerator / self._denominator, 3)

    @classmethod
    def from_float(cls, float_value: float) -> "Fraction":
        denominator = 10 ** 3
        numerator = round(float_value * denominator)
        return cls(numerator, denominator)

    @staticmethod
    def is_fraction(obj) -> bool:
        return isinstance(obj, Fraction)

# Пример использования
f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
f3 = Fraction(3, 4)

print(f"f1: {f1}")            
print(f"f2: {f2}")             
print(f"f1 is f2: {f1 is f2}")  

print(f"f1 + f3: {f1 + f3}")    
print(f"f3 - f1: {f3 - f1}")    
print(f"f1 * f3: {f1 * f3}")    
print(f"f3 / f1: {f3 / f1}")    

print(f"f1.value: {f1.value}")  

# Примеры сравнения
print(f"f1 == f2: {f1 == f2}")  
print(f"f1 < f3: {f1 < f3}")    
print(f"f3 > f1: {f3 > f1}")    
