def max_score(beers, fries):
    max_score = 0
    index = 0
    beers.sort()
    fries.sort()
    for beer in beers:
        max_score += beer * fries[index]
        index += 1
    return max_score



print(max_score([10, 11], [1, 5]))
print(max_score([5], [5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))

