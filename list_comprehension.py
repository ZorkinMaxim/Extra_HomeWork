numbers = [n for n in range(1, 11)]
print(numbers)

numbers1 = [n*n for n in range(1, 11)]
print(numbers1)

numbers2 = [n*n for n in range(1, 11) if n % 2 != 0]
print(numbers2)

len_in_centimeters = [12, 10, 54, 124, 64]
len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centimeters]
print(len_in_inches)

ratings = [2345, 6934, 2145, 3342, 1233]
titles = ['GM' if x >= 2500 else 'MM' for x in ratings]
print(titles)

list1 = [1, 3, 4, 5, 6, 7, 7, 8]
list2 = [4, 6, 2, 0, 1, 7, 3, 7]
pairs = [(x, y) for x in list1 for y in list2 if x + y == 5]
print(pairs)

