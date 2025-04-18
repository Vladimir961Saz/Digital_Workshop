# №1
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, sound):
        self._sound = sound

    @abstractmethod
    def speak(self):
        """Метод для издания звука, обязательный к переопределению"""
        pass


class MixinSwim:
    def swim(self):
        return "плавает"


class MixinFly:
    def fly(self):
        return "летает"


class Duck(Animal, MixinSwim, MixinFly):
    def __init__(self):
        super().__init__("кря-кря")

    def speak(self):
        return self._sound


class Penguin(Animal, MixinSwim):
    def __init__(self):
        super().__init__("буль-буль")

    def speak(self):
        return self._sound


animals = [Duck(), Penguin()]

for animal in animals:
    output = f"{animal.__class__.__name__}: {animal.speak()}, {animal.swim()}"
    if isinstance(animal, MixinFly):
        output += f", {animal.fly()}"
    print(output)

# №2

class Writer:
    def write(self):
        return "пишет текст"


class Painter:
    def draw(self):
        return "рисует картину"


class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение"

    def draw(self):
        return "выразительно рисует пейзаж"


persons = [
    Writer(),
    Painter(),
    CreativePerson()
]

for person in persons:
    if hasattr(person, 'write'):
        print(person.write())
    if hasattr(person, 'draw'):
        print(person.draw())
