def make_fixed_size_string(size, string):
    fixed_size_string = ""
    if len(string) >= size:
        for i in range(size):
            fixed_size_string += string[i]
    else:
        fixed_size_string = string + "X" *(size - len(string))
    return fixed_size_string

def format_string(string):
    formatted_string = "|"
    for char in string:
        formatted_string += " " + char + " |"
    formatted_string += "\n"
    return formatted_string

def string_matrix(matrix_width, strings):
    result = ""
    for index in range(len(strings)):
        strings[index] = make_fixed_size_string(matrix_width, strings[index])
        result += format_string(strings[index])
    return result


result = string_matrix(6,["python","gogo","perl","java","haskell","ruby0nRails"])
print(result)