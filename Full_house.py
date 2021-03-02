import itertools as it

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
comb3 = []
comb2 = []

for i in cards:
    comb3.append(i + i + i)
    comb2.append(i + i)

# print(comb3)
# print(comb2)

full_hous = []

for i in it.combinations(comb3, 1):
    for j in it.combinations(comb2, 1):
        full_hous.append(i + j)

# print(full_hous)


def is_full_house(comb):
    if comb in full_hous:
        return True
    else:
        return False

print(is_full_house(('555', 'KK')))
