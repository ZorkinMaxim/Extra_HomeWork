# Создайте класс Calculator который поддерживает:
# сложение двух чисел
# вычисление разницы между двумя числами
# умножение двух чисел
# деление одного числа на другое

class Calculator:

    def add(self, a, b):
        return a + b

    def subtruct(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


c = Calculator()
print(c.add(10, 5))
print(c.subtruct(10, 5))
print(c.multiply(10, 5))
print(c.divide(10, 5))
print(c.divide(10, 5).__int__())
