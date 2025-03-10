# №1
import re

class Student:
    __slots__ = ("__full_name", "__student_id", "__average_grade", "__enrollment_year")
    
    # Класс-атрибуты: счётчик объектов, компилированные регулярки и минимальный год поступления
    _student_count = 0
    _name_pattern = re.compile(r"^[A-Za-zА-Яа-яЁё-]+$")
    _id_pattern = re.compile(r"^\d{8}$")
    _MIN_ENROLLMENT_YEAR = 2000

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._student_count += 1
        return instance

    def __init__(self, full_name: str, student_id: str, average_grade: float, enrollment_year: int):
        # Используем свойства для установки с проверками
        self.full_name = full_name
        self.student_id = student_id
        self.average_grade = average_grade
        self.enrollment_year = enrollment_year

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Полное имя должно быть строкой.")
        parts = value.strip().split()
        if len(parts) != 3:
            raise ValueError("Полное имя должно состоять из трёх частей: фамилия, имя, отчество.")
        for part in parts:
            if not self._name_pattern.fullmatch(part):
                raise ValueError(f"Недопустимые символы в части имени: {part}")
        self.__full_name = value.strip()

    @property
    def student_id(self) -> str:
        return self.__student_id

    @student_id.setter
    def student_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("student_id должен быть строкой.")
        if not Student.is_valid_student_id(value):
            raise ValueError("student_id должен состоять ровно из 8 цифр.")
        self.__student_id = value

    @property
    def average_grade(self) -> float:
        return self.__average_grade

    @average_grade.setter
    def average_grade(self, value):
        try:
            grade = float(value)
        except (TypeError, ValueError):
            raise TypeError("Средний балл должен быть числом.")
        if not (0 <= grade <= 100):
            raise ValueError("Средний балл должен быть в диапазоне от 0 до 100.")
        self.__average_grade = grade

    @property
    def enrollment_year(self) -> int:
        return self.__enrollment_year

    @enrollment_year.setter
    def enrollment_year(self, value):
        try:
            year = int(value)
        except (TypeError, ValueError):
            raise TypeError("Год поступления должен быть целым числом.")
        if year < self._MIN_ENROLLMENT_YEAR:
            raise ValueError(f"Год поступления не может быть раньше {self._MIN_ENROLLMENT_YEAR} года.")
        self.__enrollment_year = year

    @staticmethod
    def is_valid_student_id(sid: str) -> bool:
        """Проверяет, что student_id состоит ровно из 8 цифр."""
        return bool(Student._id_pattern.fullmatch(sid))

    @classmethod
    def from_string(cls, data: str) -> "Student":
        """
        Создаёт объект Student из строки с данными, разделёнными запятыми.
        Ожидаемый формат: "Фамилия,Имя,Отчество,student_id,average_grade,enrollment_year"
        """
        parts = [p.strip() for p in data.split(',')]
        if len(parts) != 6:
            raise ValueError("Строка должна содержать 6 элементов, разделённых запятыми.")
        last_name, first_name, patronymic, student_id, average_grade, enrollment_year = parts
        full_name = f"{last_name} {first_name} {patronymic}"
        return cls(full_name, student_id, float(average_grade), int(enrollment_year))

    def __repr__(self):
        return (f"Student(full_name='{self.full_name}', student_id='{self.student_id}', "
                f"average_grade={self.average_grade}, enrollment_year={self.enrollment_year})")


# Пример использования:
if __name__ == '__main__':
    student1 = Student("Иванов Иван Иванович", "12345678", 85, 2021)
    print(student1)

    student2 = Student.from_string("Петров,Пётр,Петрович,87654321,90,2022")
    print(student2)

    print("Всего студентов создано:", Student._student_count)

# №2
import re

class Product:
    __slots__ = ("__name", "__price", "__quantity", "__initialized")
    # Словарь для хранения экземпляров по уникальному имени
    _instances = {}

    def __new__(cls, name: str, price: float, quantity: int):
        # Если продукт с таким именем уже создан, возвращаем существующий экземпляр
        if name in cls._instances:
            return cls._instances[name]
        instance = super().__new__(cls)
        cls._instances[name] = instance
        return instance

    def __init__(self, name: str, price: float, quantity: int):
        # Инициализация выполняется только один раз для каждого уникального экземпляра
        if getattr(self, '_Product__initialized', False):
            return
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__initialized = True

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой.")
        if not value.strip():
            raise ValueError("Название не должно быть пустым.")
        self.__name = value.strip()

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value):
        try:
            val = float(value)
        except (TypeError, ValueError):
            raise TypeError("Цена должна быть числом.")
        if val <= 0:
            raise ValueError("Цена должна быть положительным числом.")
        self.__price = val

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        try:
            val = int(value)
        except (TypeError, ValueError):
            raise TypeError("Количество должно быть целым числом.")
        if val < 0:
            raise ValueError("Количество не может быть меньше нуля.")
        self.__quantity = val

    @staticmethod
    def convert_dollars_to_euros(price: float, exchange_rate: float = 0.85) -> float:
        """
        Конвертирует цену из долларов в евро по фиксированному курсу.
        По умолчанию используется курс 0.85.
        """
        try:
            price_val = float(price)
        except (TypeError, ValueError):
            raise TypeError("Цена должна быть числом.")
        if price_val < 0:
            raise ValueError("Цена не может быть отрицательной для конвертации.")
        return price_val * exchange_rate

    @classmethod
    def from_string(cls, data: str) -> "Product":
        """
        Создает объект Product из строки формата "name;price;quantity".
        """
        parts = data.split(';')
        if len(parts) != 3:
            raise ValueError("Строка должна содержать 3 элемента, разделенных ';'.")
        name, price, quantity = (part.strip() for part in parts)
        return cls(name, float(price), int(quantity))

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


# Примеры использования:
if __name__ == '__main__':
    # Создание товаров
    p1 = Product("Молоко", 1.2, 100)
    print(p1)

    p2 = Product("Хлеб", 0.8, 50)
    print(p2)

    # Попытка создать товар с тем же именем "Молоко"
    p3 = Product("Молоко", 1.5, 80)
    print(p3)
    print("p1 is p3:", p1 is p3)  # True, так как оба экземпляра ссылаются на один объект

    # Конвертация цены из долларов в евро
    euro_price = Product.convert_dollars_to_euros(p1.price)
    print("Цена в евро:", euro_price)

    # Создание товара из строки
    p4 = Product.from_string("Яйца;2.5;200")
    print(p4)
