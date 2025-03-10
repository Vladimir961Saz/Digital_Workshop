from math import gcd

class Fraction:
    
    def __init__(self, numerator: int, denominator: int):
        common_divisor = gcd(numerator, denominator)
        # Корректно обрабатываем знак: знаменатель всегда положительный
        self._numerator = (numerator // common_divisor) * (-1 if denominator < 0 else 1)
        self._denominator = abs(denominator // common_divisor)

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"
    
    def _operate(self, other: "Fraction", op) -> "Fraction":
        num1, denom1 = self._numerator, self._denominator
        num2, denom2 = other._numerator, other._denominator
        return Fraction(op(num1 * denom2, num2 * denom1), denom1 * denom2)
    
    def __add__(self, other: "Fraction",) -> "Fraction":
        return self._operate(other, lambda x, y: x + y)

    def __sub__(self, other: "Fraction") -> "Fraction":
        return self._operate(other, lambda x,y: x - y)
    
    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction (self._numerator * other._numerator, self._denominator * other._denominator)
    
    def __truediv__(self, other: "Fraction") -> "Fraction":
        if other._numerator == 0:
            raise ZeroDivisionError("Нельзя делить на дробь с нулевым числителем")
        return Fraction(self._numerator * other._denominator, self._denominator * other._numerator)
    
    @property
    def value (self) -> float:
        # (Возвращаем десятичное значение дроби, округленное до 3 знаков)
        return round(self._numerator / self._denominator, 3)
    
    @classmethod
    def from_float(cls, float_value: float) ->
    

    