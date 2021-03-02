# Joined list
# Взять из первого списка все нечетные числа, из второго все четные и объеденить их в новом спике joined_list.

# variation 1
first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

joined_list = []
for x in first_list:
    if x % 2 != 0:
        joined_list.append(x)
for x in second_list:
    if x % 2 == 0:
        joined_list.append(x)
print(f'Joined list: {joined_list}')

# variation 2
first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

odds = [x for x in first_list if x % 2 != 0]
evens = [x for x in second_list if x % 2 == 0]
joined_list = odds + evens
print(f'Joined list: {joined_list}')
