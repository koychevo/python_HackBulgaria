a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = int(input("Enter x: "))

if x < a:
    print("The number is outside the interval, x < a")
elif x == a:
    print("The number is equal to the lower bound of the interval")
elif a < x < b:
    print("The number is in the interval")
elif x == b:
    print("he number is equal to the upper bound of the interval")
elif x > b:
    print("The number is outside the interval, x > b")