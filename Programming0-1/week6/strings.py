def str_reverse(string):
    reverse_string = ""
    for i in range(len(string) - 1, -1, -1):
        reverse_string += string[i]
    return reverse_string

#print(str_reverse("Python"))
#print(str_reverse("kapak"))
#print(str_reverse(""))


def join(delimiter, items):
    string = ""
    last_index = len(items) - 1
    for i in range(last_index):
        string += items[i] + delimiter
    string += items[last_index]
    return string

#print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))
#print(join("\n", ["line1", "line2"]))


def startswith(search, string):
    search_len = len(search)
    string_len= len(string)
    first_part = ""
    if search_len > string_len:
        return False
    for i in range(search_len):
        first_part += string[i]
    if first_part != search:
        return False
    return True

#print(startswith("Py", "Python"))
#print(startswith("py", "Python"))
#print(startswith("baba", "asdbaba"))


def endswith(search, string):
    string = str_reverse(string)
    search = str_reverse(search)
    return startswith(search, string)

#print(endswith(".py", "hello.py"))
#print(endswith("kapak", "babakapak"))
#print(endswith(" ", "Python   "))
#print(endswith("py", "python"))

def trim(string):
    left_counter = 0
    right_counter = 0
    result = ""

    for i in range(len(string)):
        if string[i] == " ":
            left_counter += 1
        else:
            break

    for i in range(len(string) - 1, -1, -1):
        if string[i] == " ":
            right_counter += 1
        else:
            break

    for i in range(left_counter, len(string) - right_counter):
        result += string[i]
    return result

print(trim("   asdt   "))
print(trim(" spacious    "))
print(trim("no here but yes at end   "))
print(trim("                      "))
print(trim("python"))