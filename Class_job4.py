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
