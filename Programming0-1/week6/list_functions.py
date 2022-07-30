def head(items):
    return items[0]

#print(head([1, 2, 3]))
#print(head(["Python"]))

def last(items):
    return items[len(items) - 1]

#print(last([1, 2, 3]))
#print(last(["Python"]))

def tail(items):
    new_items = []
    for i in range(1, len(items)):
        new_items += [items[i]]
    return new_items

#print(tail([1, 2, 3]))
#print(tail(["Python"]))

def equal_lists(first_items, second_items):
    len_first_items = len(first_items)
    len_second_items = len(second_items)
    if len_first_items != len_second_items:
        return False
    for i in range(len_first_items):
        if first_items[i] != second_items[i]:
            return False
    return True

#print(equal_lists([1, 2], [1, 2]))
#print(equal_lists([1, 2], [2, 1]))
#print(equal_lists([], []))

def count_item(element, items):
    counter = 0
    for item in items:
        if item == element:
            counter += 1
    return counter

#print(count_item(5, [1, 2, 3, 4, 5]))
#print(count_item("winter", ["winter", "winter"]))
#print(count_item(False, [True, True]))

def take(number, items):
    result = []
    length = len(items)
    if number > length:
        number = length
    for i in range(number):
        result += [items[i]]
    return result

#print(take(2, [1, 2, 3, 4, 5]))
#print(take(3, [3, 4, 5, 6, 7, 8]))
#print(take(10, [1]))

def drop(number, items):
    result = []
    for i in range(number, len(items)):
        result += [items[i]]
    return result

#print(drop(1, [1, 2, 3]))
#print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
#print(drop(10, [1]))

def reverse(items):
    reverse_items = []
    for item in items:
        reverse_items = [item] + reverse_items
    return reverse_items

print(reverse(["Speak", "in", "reverse", "you", "must!"]))
print(reverse([1, 2, 3]))
print(reverse([]))
