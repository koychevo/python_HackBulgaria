def sum_items(items):
    sum = 0
    for item in items:
        sum += item
    return sum

def loss_or_profit(income, outcome):
    income_sum = sum_items(income)
    outcome_sum = sum_items(outcome)
    total = income_sum - outcome_sum
    if total < 0:
        return str(total)
    elif total > 0:
        return "+" + str(total)
    else:
        return "=0"

print(loss_or_profit([1, 2, 3], [3]))
print(loss_or_profit([10], [20, 30]))
print(loss_or_profit([10], [10]))