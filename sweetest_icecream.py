class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

    @staticmethod
    def sweetest_icecream(lst):
        flavor_values = {
            'Plain': 0,
            'Vanilla': 5,
            'ChocolateChip': 5,
            'Strawberry': 10,
            'Chocolate': 10
        }
        return max([icecream.sprinkles + flavor_values[icecream.flavor] for icecream in lst])


ice1 = IceCream("Chocolate", 13)  # 10 + 13 = 23
ice2 = IceCream("Vanilla", 0)  # 5 + 0 = 5
ice3 = IceCream("Strawberry", 7)  # 10 + 7 = 17
ice4 = IceCream("Plain", 18)  # 0 + 18 = 18
ice5 = IceCream("ChocolateChip", 3)  # 5 + 3 = 8

print(f"The sweetest Ice Cream has a level = {IceCream.sweetest_icecream([ice1, ice2, ice3, ice4, ice5])}")
