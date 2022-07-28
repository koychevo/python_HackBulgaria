def slice_list(items, start, count):
    sliced_list = []
    for i in range(start, start + count):
        sliced_list += [items[i]]
    return sliced_list


def sublist(first_list, second_list):
    n = len(first_list)
    if n == 0:
        return True
    index = 0
    while index <= len(second_list) - n:
        sublist = slice_list(second_list, index, n)
        if first_list == sublist:
            return True
        index += 1
    return False


print(sublist(["Python"],["Python", "Django"]))
print(sublist(["Python", "Django"], ["Django", "Python"]))
print(sublist([1,2], [1, 0, 1, 2, 2]))
print(sublist([1, 2, 3], [0, 0, 1, 2, 3, 5, 6]))
