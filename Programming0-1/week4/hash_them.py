def hash_them(keys, values):
    index = 0
    result = {}
    for key in keys:
        if index >= len(values):
            result[key] = None
        else:
            result[key] = values[index]
        index += 1
    return result

print(hash_them(["Ivan", "Maria"], [1, 2]))
print(hash_them(["Ivan", "Maria"], [1]))