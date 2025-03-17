# №1
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.__account_number, self.__balance = account_number, balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        return "Invalid or insufficient funds."

    def get_balance(self):
        return f"Account balance: {self.__balance}"

    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)


# Пример использования
account = BankAccount.create_empty_account("12345678")
print(account.deposit(1000))
print(account.withdraw(500))
print(account.get_balance())



# №2
class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        if self.__is_strong_password(password):
            self.__password = password
        else:
            raise ValueError("Пароль слишком простой. Должен быть не менее 6 символов.")

    @staticmethod
    def __is_strong_password(password: str) -> bool:
        return len(password) >= 6

    @classmethod
    def create_with_default_password(cls, username: str):
        return cls(username, "default123")  # Безопасный пароль по умолчанию

    def change_password(self, new_password: str):
        if self.__is_strong_password(new_password):
            self.__password = new_password
            print("Пароль успешно изменён.")
        else:
            print("Ошибка: Новый пароль слишком простой.")

    def get_username(self):
        return self.__username

# Пример использования
user1 = User("Alice", "securePass")
print(user1.get_username())

user2 = User.create_with_default_password("Bob")
print(user2.get_username())

user2.change_password("newpass")  # Ошибка
user2.change_password("strongpassword")  # Успех

class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        if self.__is_strong_password(password):
            self.__password = password
        else:
            raise ValueError("Пароль слишком простой. Должен быть не менее 6 символов.")

    @staticmethod
    def __is_strong_password(password: str) -> bool:
        return len(password) >= 6

    @classmethod
    def create_with_default_password(cls, username: str):
        return cls(username, "default123")  # Безопасный пароль по умолчанию

    def change_password(self, new_password: str):
        if self.__is_strong_password(new_password):
            self.__password = new_password
            print("Пароль успешно изменён.")
        else:
            print("Ошибка: Новый пароль слишком простой.")

    def get_username(self):
        return self.__username

# Пример использования
user1 = User("Alice", "securePass")
print(user1.get_username())

user2 = User.create_with_default_password("Bob")
print(user2.get_username())

user2.change_password("newpass")  # Ошибка
user2.change_password("strongpassword")  # Успех


# №3
class Book:
    def __init__(self, title: str, author: str, year: int):
        if self.__is_valid_year(year):
            self.__title = title
            self.__author = author
            self.__year = year
        else:
            raise ValueError("Некорректный год издания.")

    @staticmethod
    def __is_valid_year(year: int) -> bool:
        from datetime import datetime
        current_year = datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_without_year(cls, title: str, author: str):
        return cls(title, author, 2024)

    def get_info(self) -> str:
        return f"{self.__title} - {self.__author} ({self.__year})"

# Пример использования
book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())

book2 = Book.create_without_year("New Book", "Unknown Author")
print(book2.get_info())
