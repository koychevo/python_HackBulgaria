def decode_word(encrypted_word, cipher):
    decoded_word = ""
    decoded_cipher = {}

    for index in cipher:
        decoded_cipher[cipher[index]] = index

    for char in encrypted_word:
        decoded_word += decoded_cipher[char]

    return decoded_word

print(decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))
print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}))
print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))
print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))