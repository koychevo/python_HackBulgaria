string = input()

vowels = "aeiouy"
vowels_counter = 0

for char in string.lower():
    if char in vowels:
        vowels_counter += 1

print(vowels_counter)
