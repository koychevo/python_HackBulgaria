a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter operation: ")

calculation = 0

if op == "+":
    calculation = a + b
elif op == "-":
    calculation = a - b
elif op == "*":
    calculation = a * b
elif op == "/":
    if b == 0:
        print("The number can not be divided by zero.")
        exit()
    calculation = a / b
else:
    print("We do not support that operation.")
    exit()

print(f"Result is: {calculation}")