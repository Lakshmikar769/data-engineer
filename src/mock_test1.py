i = int(input("Enter a number: "))
for i in range(1, i + 1):
    print(i)

    # prime number
number = int(input("Enter a number: "))
def is_prime(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return false
        else:
            return true
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")