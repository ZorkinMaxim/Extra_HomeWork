# Создать класс Beverage, который при конструировании принимает список ингредиентов
# поддерживает атрибут ingredients, возвращающий список ингредиентов, переданных при конструировании инстанции класса
# поддерживает функцию get_cost, вычисляющую итоговую стоимость всех ингредиентов напитка
# (получается себестоимость напитка)
# поддерживает функцию get_price, вычисляющую цену напитка посредством умножения себестоимости на 2.5
# поддерживает функцию get_name, которая возвращает строку, перечисляющую ингредиенты, сортируя их в алфавитном порядке.
# Если ингредиентов больше одного, то в конце добавляет слово 'Fusion', иначе добавляет слово 'Smoothie'.
# Эта функция также должна заменять 'berries' на 'berry'.
# Ингредиенты и их себестоимость
# Strawberries $1.50
# 2 Banana $0.50
# 3 Mango $2.50
# 4 Blueberries $1.00
# 5 Raspberries $1.00
# 6 Apples $1.75
# 7 Pineapple $3.50

prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5, "Blueberries": 1, "Raspberries": 1,
          "Apple": 1.75, "Pineapple": 3.5}


class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.price:.2f}'

    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'


b1 = Beverage(["Banana"])
print(b1.ingredients)
print(b1.get_cost())
print(b1.get_price())
print(b1.get_name())

b2 = Beverage(["Raspberries"])
print(b2.ingredients)
print(b2.get_cost())
print(b2.get_price())
print(b2.get_name())

b3 = Beverage(["Raspberries", "Apple", "Pineapple", "Strawberries", "Banana", "Mango"])
print(b3.ingredients)
print(b3.get_cost())
print(b3.get_price())
print(b3.get_name())

