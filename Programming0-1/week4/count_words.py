def count_words(words):
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return  words_dict

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))