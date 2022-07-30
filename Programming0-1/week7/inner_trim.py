def left_trim(string):
    trimmed_string = ""
    start_index = 0
    for i in range(len(string)):
        if string[i] == " ":
            start_index += 1
        else:
            break
    if start_index > 0:
        for i in range(start_index, len(string)):
            trimmed_string += string[i]
    else:
        trimmed_string = string
    return trimmed_string


def right_trim(string):
    trimmed_string = ""
    last_index = len(string) - 1
    for i in range(len(string) - 1, -1, -1):
        if string[i] == " ":
            last_index -= 1
        else:
            break
    if last_index < len(string) - 1:
        for i in range(last_index + 1):
            trimmed_string += string[i]
    else:
        trimmed_string = string
    return trimmed_string


def inner_trim(string):
    trimmed_string = ""
    string = left_trim(right_trim(string))
    is_char_space = False
    for index in range(len(string)):
        if ord(string[index]) == 32 and not is_char_space:
            trimmed_string += string[index]
            is_char_space = True
        elif ord(string[index]) != 32:
            trimmed_string += string[index]
            is_char_space = False

    string = right_trim(left_trim(string))
    return trimmed_string



print(inner_trim("I         am") + "!")
print(inner_trim("       Take    me  down to the            paradise                city") + "!")
print(inner_trim("Python    Django"))
print(inner_trim("  Python     Django   "))