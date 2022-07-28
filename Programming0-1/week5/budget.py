def on_budget(books, budget):
    result = {
        "books_on_budget": 0,
        "loan": 0
    }
    books.sort()
    total_sum = 0
    for book in books:
        if book <= budget:
            result["books_on_budget"] += 1
            budget -= book
        else:
            total_sum += book
    if total_sum > budget:
        result["loan"] = total_sum - budget
    return result


print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 100], 20))
