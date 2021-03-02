# Создайте класс Pizza, который принимает список ингредиентов.
# Класс поддерживает:
# атрибут order_number, который возвращает текущий номер заказа
# (подсказка: используйте статический атрибут в качестве сквозного счётчика)
# атрибут ingredients, который возвращает список, принятый в конструкторе
# функции (garden_feast, hawaiian, meat_festival) создания видов пицц,
# ингредиенты которых заранее известны (см. таблицу)
# Name            Ingredients
# hawaiian            - ham, pineapple
# meat_festival    - beef, meatball, bacon
# garden_feast    - spinach, olives, mushroom

class Pizza:
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


p1 = Pizza(['ham', 'bacon'])
p2 = Pizza.hawaiian()
p3 = Pizza.garden_feast()
p4 = Pizza(['beef', 'olives'])

print(Pizza.order)
print(p1.order_number)
print(p2.order_number)
print(p2.ingredients)
print(p3.order_number)
print(p3.ingredients)
print(p4.order_number)
print(p4.ingredients)
