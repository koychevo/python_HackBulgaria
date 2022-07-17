n = int(input("Enter n: "))
m = int(input("Enter m: "))

last_digit_n = n % 10
last_digit_m = m % 10

if last_digit_n > last_digit_m:
    print(n)
elif last_digit_n < last_digit_m:
    print(m)
elif n < m:
    print(m)
elif n > m:
    print(n)
else:
    print(f"The numbers are equal! {n}")