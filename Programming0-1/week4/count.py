def count_vowels_consonants(word):
    letters = {
        "vowels": 0,
        "consonants": 0
    }
    word = word.lower()
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "y"]:
            letters["vowels"] += 1
        else:
            letters["consonants"] += 1
    return letters


print(count_vowels_consonants("aaaAcccDpp"))