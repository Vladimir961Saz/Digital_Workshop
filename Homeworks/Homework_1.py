# №1
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

# №2
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
r.height = 25 # Успешно

try:
    r.color = 'red'  
except AttributeError as e:
    print(e)  
