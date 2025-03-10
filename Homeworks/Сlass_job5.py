# №1
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
        # Вспомогательный метод для операций сложения и вычитания
        num1, denom1 = self._numerator, self._denominator
        num2, denom2 = other._numerator, other._denominator
        return Fraction(op(num1 * denom2, num2 * denom1), denom1 * denom2)

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

    @property
    def value(self) -> float:
        # Возвращаем десятичное значение дроби, округленное до 3 знаков
        return round(self._numerator / self._denominator, 3)

    @classmethod
    def from_float(cls, float_value: float) -> "Fraction":
        # Преобразование числа с плавающей точкой в дробь с точностью до 3 знаков после запятой
        denominator = 10 ** 3
        numerator = round(float_value * denominator)
        return cls(numerator, denominator)

    @staticmethod
    def is_fraction(obj) -> bool:
        return isinstance(obj, Fraction)

# Пример использования:
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)  # 5/4
print(f1 - f2)  # -1/4
print(f1 * f2)  # 3/8
print(f1 / f2)  # 2/3
print(f1.value) # 0.5


# №2

class FractionMatrix:
    def __new__(cls, matrix: list[list["Fraction"]]):
        if not isinstance(matrix, list) or not matrix:
            raise ValueError("Матрица должна быть непустым списком списков")
        row_length = len(matrix[0])
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                raise ValueError("Все строки матрицы должны быть списками одинаковой длины")
            for elem in row:
                if not Fraction.is_fraction(elem):
                    raise TypeError("Все элементы матрицы должны быть экземплярами класса Fraction")
        return super().__new__(cls)

    def __init__(self, matrix: list[list["Fraction"]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self) -> str:
        # Красивый вывод: каждая строка матрицы выводится на отдельной строке
        return "\n".join("  ".join(str(elem) for elem in row) for row in self.matrix)

    @staticmethod
    def _compute_determinant(matrix: list[list["Fraction"]]) -> "Fraction":
        n = len(matrix)
        # Базовые случаи
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = Fraction(0, 1)
        for col in range(n):
            # Формируем минор, исключая 0-ю строку и столбец col
            submatrix = [
                [matrix[i][j] for j in range(n) if j != col]
                for i in range(1, n)
            ]
            sign = Fraction(1, 1) if col % 2 == 0 else Fraction(-1, 1)
            det = det + sign * matrix[0][col] * FractionMatrix._compute_determinant(submatrix)
        return det

    @property
    def determinant(self) -> "Fraction":
        if self.rows != self.cols:
            raise ValueError("Определитель можно вычислить только для квадратных матриц")
        return FractionMatrix._compute_determinant(self.matrix)

    def __add__(self, other: "FractionMatrix") -> "FractionMatrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Для сложения матриц они должны иметь одинаковые размеры")
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return FractionMatrix(result)

    def __sub__(self, other: "FractionMatrix") -> "FractionMatrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Для вычитания матриц они должны иметь одинаковые размеры")
        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return FractionMatrix(result)

    def __mul__(self, other: "FractionMatrix") -> "FractionMatrix":
        if self.cols != other.rows:
            raise ValueError("Невозможно перемножить матрицы: число столбцов первой матрицы должно совпадать с числом строк второй")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                cell = Fraction(0, 1)
                for k in range(self.cols):
                    cell = cell + self.matrix[i][k] * other.matrix[k][j]
                row.append(cell)
            result.append(row)
        return FractionMatrix(result)

    def transpose(self) -> "FractionMatrix":
        # Транспонирование матрицы
        transposed = [
            [self.matrix[i][j] for i in range(self.rows)]
            for j in range(self.cols)
        ]
        return FractionMatrix(transposed)

    @classmethod
    def identity(cls, n: int) -> "FractionMatrix":
        # Создание единичной матрицы n x n
        matrix = [
            [Fraction(1, 1) if i == j else Fraction(0, 1) for j in range(n)]
            for i in range(n)
        ]
        return cls(matrix)

    @staticmethod
    def are_same_dimensions(m1: "FractionMatrix", m2: "FractionMatrix") -> bool:
        return m1.rows == m2.rows and m1.cols == m2.cols

# Пример использования (предполагается, что класс Fraction уже определён):
m1 = FractionMatrix([
    [Fraction(1, 2), Fraction(1, 3)],
    [Fraction(2, 5), Fraction(3, 4)]
])
m2 = FractionMatrix([
    [Fraction(1, 3), Fraction(2, 3)],
    [Fraction(1, 2), Fraction(2, 5)]
])

print("m1 + m2:")
print(m1 + m2)
print("\nm1 * m2:")
print(m1 * m2)
print("\nОпределитель m1:")
print(m1.determinant)
print("\nТранспонированная m1:")
print(m1.transpose())
