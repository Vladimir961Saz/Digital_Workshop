# №1
class Sauce:
    base = "Olive oil"
    def __init__(self, flavor=None):
        self.flavor = flavor

    def show_my_sauce(self):
        if self.flavor:
            print(f"Соус: {self.flavor}")
        else:
            print(str(Sauce.base))

sauce1 = Sauce("Чесночный")
sauce1.show_my_sauce()  # Вывод: Соус: Чесночный

sauce2 = Sauce()
sauce2.show_my_sauce()  # Вывод: Майонез

# №2

class Employee:
    SALARY = 50000
    def __init__(self, name, age):
        self.name = name         
        self._age = age          
        self.__salary = Employee.SALARY
        self.__bonus = 0
            

    def get_name(self):
        print( self.name)
    
    def get_age(self):
        print( self._age)
    
    def get_salary(self):
        print( self.__salary)
    
    def get_bonus(self):
        print( self.__bonus)
    
    def set_bonus(self, x):
        self.__bonus = x

    def get_total_salary(self):
        print( self.__salary + self.__bonus)
    
pt = Employee('Max',19)
pt.get_name()
pt.get_age()
pt.get_salary()
pt.get_bonus()
pt.set_bonus(99999)
pt.get_total_salary()



# №3

class Recipe:
    def __init__(self, name,ingredients):
        self.name = name         
        self.ingredients = ingredients         

    def print_ingredients(self):
        print(f'Ингредиенты для {self.name}:')
        for i in self.ingredients:
            print(f'- {i}')
    
    def cook(self):
        print( f'Сегодня мы готовим {self.name}.')
        print( f'Выполняем инструкцию по приготовлению блюда {self.name}...')
        print( f'Блюдо {self.name} готово!')

# создаем рецепт спагетти болоньезе
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# печатаем список продуктов для рецепта спагетти
spaghetti.print_ingredients()

# готовим спагетти
spaghetti.cook()  

# создаем рецепт для кекса
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

# печатаем рецепт кекса
cake.print_ingredients()

# готовим кекс
cake.cook()


