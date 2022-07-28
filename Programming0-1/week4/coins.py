def calculate_coins(sum):
    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum = int(sum * 100)
    for coin in coins:
        result[coin] = sum // coin
        sum = sum % coin
    return result

print(calculate_coins(0.53))
print(calculate_coins(8.94))

