#Запросить у пользователя ввод числа. Построить цикл от 0 до введённого числа (включительно) и для чётных чисел вывести то,
# что они чётные, а для нечётных, что они нечётные.
# Пример вывода:
# 0 is EVEN
# 1 is ODD
# 2 is EVEN

limit = int(input('Enter the limit'))

for x in range(limit + 1):
    if x % 2 == 0:
        print(f'{x} is Even')
    else:
        print(f'{x} is Odd')
