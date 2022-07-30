def taken_name(surname_husband, surname_wife):
    index = -1
    for i in range(len(surname_wife)):
        if surname_wife[i] == "-":
            index = i + 1
            break
    if index > -1:
        wife_surname = ""
        for i in range(index, len(surname_wife)):
            wife_surname += surname_wife[i]
        surname_wife = wife_surname
    if surname_wife == surname_husband + "a":
        return True
    return False

print(taken_name("Petrov", "Petrova"))
print(taken_name("Ivanov", "Tsvetanova"))
print(taken_name("Petrov", "Ivanova-Petrova"))