# №1
import timeit
import sys


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ('x', 'y', '_z')

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        """Свойство для только чтения координаты z"""
        return self._z

    @z.setter
    def z(self, value):
        raise AttributeError("Изменение атрибута z запрещено!")

    def __getattribute__(self, name):
        if name == '__dict__':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '__dict__'")
        return super().__getattribute__(name)


if __name__ == '__main__':
    pt3 = Point3D(10, 20, 30)
    print("pt3.z =", pt3.z)

    try:
        pt3.z = 40
    except AttributeError as e:
        print("Ошибка при изменении pt3.z:", e)

    try:
        print(pt3.__dict__)
    except AttributeError as e:
        print("Ошибка при обращении к pt3.__dict__:", e)

    print("pt3.__slots__:", pt3.__slots__)
    print("pt3.x =", pt3.x)

# №2


class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class SlotPoint:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def create_points(cls, num=1000):
    return [cls(0, 0) for _ in range(num)]


normal_points = create_points(NormalPoint)
slot_points = create_points(SlotPoint)


def test_normal_points():
    for p in normal_points:
        p.move(1, 1)


def test_slot_points():
    for p in slot_points:
        p.move(1, 1)


time_normal = timeit.timeit(test_normal_points, number=1000)
time_slot = timeit.timeit(test_slot_points, number=1000)

print("Время выполнения для NormalPoint:", time_normal)
print("Время выполнения для SlotPoint:", time_slot)


normal_size = sys.getsizeof(normal_points[0])
slot_size = sys.getsizeof(slot_points[0])

print("Размер объекта NormalPoint (без учёта __dict__):", normal_size, "байт")
print("Размер объекта SlotPoint:", slot_size, "байт")


normal_dict_size = sys.getsizeof(normal_points[0].__dict__)
print("Размер __dict__ для NormalPoint:", normal_dict_size, "байт")


# №3
class Student:
    __slots__ = ['name', 'age', 'grade']

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


students = [
    Student("Иван", 20, 85),
    Student("Мария", 19, 92),
    Student("Петр", 21, 78),
    Student("Анна", 20, 88)
]


def average_grade(students):
    if not students:
        return 0
    total = sum(student.grade for student in students)
    return total / len(students)


avg = average_grade(students)
print("Средняя оценка студентов:", avg)

# №4


class Product:
    __slots__ = ['name', 'price', 'quantity']

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products = {
    "Ноутбук": Product("Ноутбук", 1500, 10),
    "Смартфон": Product("Смартфон", 800, 25),
    "Планшет": Product("Планшет", 600, 15),
    "Наушники": Product("Наушники", 120, 50),
    "Монитор": Product("Монитор", 300, 8)
}


def products_above_price(products_dict, threshold):
    result = []
    for product in products_dict.values():
        if product.price > threshold:
            result.append(product.name)
    return result


threshold_price = 500
expensive_products = products_above_price(products, threshold_price)
print("Товары с ценой выше", threshold_price, ":", expensive_products)
