def number_to_list(number):
    items = []
    while number != 0:
        items += [number % 10]
        number //= 10
    return items

def list_to_number(items):
    length = len(items)
    number = 0
    for index in range(length):
        number += items[index] * 10 ** (length - 1 - index)
    return number

def list_to_biggest_number(items):
    items = sorted(items, reverse = True)
    return list_to_number(items)

def list_to_smallest_number(items):
    items = sorted(items)
    return list_to_number(items)


n = int(input("Enter n: "))
items = number_to_list(n)

print(f"Largest: {list_to_biggest_number(items)}")
print(f"Smallest: {list_to_smallest_number(items)}")

