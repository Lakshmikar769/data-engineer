#Create a decorator that logs the name of the function which s being called, the arguments passed and return value of the function

import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet(name):
    return f"Hello, {name}!"

add_result = add(3, 5)
greet_result = greet("Alice")


#Create cutsomRange() iterator class, Range() using ierators

class CustomRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else:
            next_value = self.current
            self.current += self.step
            return next_value
for num in CustomRange(5):
    print(num)

print("---")

for num in CustomRange(2, 10, 2):
    print(num)

print("---")

for num in CustomRange(10, 2, -2):
    print(num)

# prime number generation using the generators

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
prime_gen = generate_primes()
for _ in range(15):
    print(next(prime_gen))