from random import randint

n = int(input("Enter sides: "))
sum = 0

dice = randint(1, n)
sum += dice
print(f"First roll: {dice}")

dice = randint(1, n)
sum += dice
print(f"Second roll: {dice}")

dice = randint(1, n)
sum += dice
print(f"Third roll: {dice}")

print(f"Sum is: {sum}")