import math
import numpy as np
import matplotlib.pyplot as plt


class Derivative:
    def __init__(self, h=1e-5):
        self.h = h

    def __get__(self, instance, owner):

        self.instance = instance
        return self

    def __call__(self, x):
        h = self.h

        return (self.instance(x + h) - self.instance(x - h)) / (2 * h)


class ExponentialFunction:

    derivative = Derivative()

    def __init__(self, a):
        self.a = a

    def __call__(self, x):

        return self.a * math.exp(x)

    def plot(self):

        x = np.linspace(-2, 2, 400)

        y = np.array([self(xi) for xi in x])
        y_prime = np.array([self.derivative(xi) for xi in x])

        # Строим графики
        plt.figure(figsize=(8, 6))
        plt.plot(
            x, y, label=f'f(x) = {self.a} * exp(x)', color='blue', linewidth=(4))
        plt.plot(x, y_prime, label="f'(x)", color='red',
                 linestyle='--', linewidth=(4))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Экспоненциальная функция и её производная')
        plt.legend()
        plt.grid(True)
        plt.show()


# Пример использования:
if __name__ == '__main__':
    exp_func = ExponentialFunction(a=2)
    print(exp_func(0))           
    print(exp_func.derivative(0))
    exp_func.plot()
