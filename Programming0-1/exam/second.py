def second_largest(numbers):
    if len(numbers) < 2:
        return False
    numbers = sorted(numbers, reverse=True)
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[0]:
            return numbers[index]
    return False

print(second_largest([]))
print(second_largest([2, 1]))
print(second_largest([5, 5]))
print(second_largest([80, 100, 100, 90]))

