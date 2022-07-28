def count_zero_pairs(numbers):
    length = len(numbers)
    count = 0
    for i in range(length):
        for j in range(i, length):
            if numbers[i] + numbers[j] == 0:
                count += 1
    return count

print(count_zero_pairs([0, 2, -2, 5, 10]))