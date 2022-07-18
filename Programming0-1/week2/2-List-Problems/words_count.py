searched_word = input("Enter word: ")
n = int(input("Enter n: "))

words = []
count = 0

for i in range(n):
    words += [input("Write word: ")]

for word in words:
    if word == searched_word:
        count += 1

print(f"{searched_word} is found {count} times.")