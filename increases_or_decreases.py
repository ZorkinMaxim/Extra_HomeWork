# def check_sequence(lst):
#     if lst[0] < lst[1] < lst[2]:
#         return 1
#     elif lst[0] > lst[1] > lst[2]:
#         return -1
#     else:
#         return 0
#
# check_sequence([3, 2, 1])

def check_sequence(lst):
    if sorted(set(lst)) == lst:
        return 1
    elif sorted(set(lst), reverse=True) == lst:
        return -1
    else:
        return 0


print(check_sequence([1, 2, 3, 4, 1]))
