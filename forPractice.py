# find all pairs sum of which equals 5

list1 = [1, 3, 4, 5, 6, 7, 7, 8]
list2 = [4, 6, 2, 0, 1, 7, 3, 7]

pairs = []
for x in list1:
    for y in list2:
        our_sum = x + y
        if our_sum == 5:
            pairs.append((x, y))
print(pairs)
