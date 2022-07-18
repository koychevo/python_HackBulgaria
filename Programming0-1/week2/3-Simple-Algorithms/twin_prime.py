p = int(input("Enter p: "))

is_p_prime = True
is_q_prime = True
is_q1_prime = True

q = p - 2
q1 = p + 2

for number in range(2, p):
    if p % number == 0:
        is_p_prime = False
        break

for number in range(2, q):
    if q % number == 0:
        is_q_prime = False
        break

for number in range(2, q1):
    if q1 % number == 0:
        is_q1_prime = False
        break


if not is_p_prime:
    print(f"{p} is not prime")

if is_p_prime and not is_q_prime and not is_q1_prime:
        print(f"{p} is prime but:")
        print(f"{q} is not")
        print(f"{q1} is not")
elif not is_p_prime:
    print(f"{p} is not prime")
else:
    print(f"Twin primes with {p}:")
    if is_q_prime:
        print(f"{q}, {p}")
    if is_q1_prime:
        print(f"{p}, {q1}")