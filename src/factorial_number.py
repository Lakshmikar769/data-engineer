def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("factorial number: "))
fact = factorial(num)
print(f"Factorial of {num} is: {fact}")