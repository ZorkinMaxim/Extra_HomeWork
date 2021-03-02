# Division by 3 or 5
# Построить от 0 до введенного числа (включительно) и посчитать сумму всех чисел, делимых без остатка на 3 или 5.
# Вывести на консоль это число

# variation 1

limit = int(input('Enter the limit'))

total_sum = 0
for x in range(limit + 1):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x
    else:
        continue
print(f'Total sum = {total_sum}')

# variation 2

limit = int(input('Enter the limit'))

total_sum = sum([x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0])
print(f'Total sum = {total_sum}')
# or print(total_sum)
