# №1
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        if key == "name" and (not isinstance(value, str) or len(value) == 0):
            raise ValueError("Имя не может быть пустым.")
        if key == "age" and (not isinstance(value, (int, float)) or value <= 0):
            raise ValueError("Возраст должен быть положительным числом.")

        super().__setattr__(key, value)


# Примеры использования:
p = Person("John", 25)
p.name = "Alice"
p.age = 30

try:
    p.name = ""
except ValueError as e:
    print(e)

try:
    p.age = -5
except ValueError as e:
    print(e)


# №2
class Counter:
    def __getattribute__(self, name):
        print(f"Доступ к атрибуту {name}")
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return None


# Пример использования:
c = Counter()
c.value = 5         # Атрибут value будет добавлен
print(c.value)      # Выведет: Доступ к атрибуту value → 5
print(c.name)       # Выведет: Доступ к атрибуту name → None


# №3
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, name):
        return "This attribute is not available"


# Пример использования:
c = Car("Toyota", "Corolla")
print(c.make)
print(c.color)


# №4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name not in ("width", "height"):
            raise AttributeError("Local attributes are not allowed")
        object.__setattr__(self, name, value)


# Пример использования:
r = Rectangle(10, 20)
r.width = 15  # Успешно
r.height = 25  # Успешно

try:
    r.color = 'red'
except AttributeError as e:
    print(e)
