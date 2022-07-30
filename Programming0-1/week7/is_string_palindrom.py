def string_only_with_small_letters(string):
    string = string.lower()
    string_only_letters = ""
    for char in string:
        if ord(char) < 97 or ord(char) > 122:
            continue
        string_only_letters += char
    return string_only_letters

def is_string_palindrom(string):
    string = string_only_with_small_letters(string)
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True



print(is_string_palindrom("Az obi4am ma4 i boza")) #True
print(is_string_palindrom("A Toyota!")) #True
print(is_string_palindrom("bozaaa")) #False
print(is_string_palindrom(" kapak! ")) #True