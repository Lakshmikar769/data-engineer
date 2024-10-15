import random

random_number = random.randint(1, 20)

while guess != random_number:
    guess = int(input("Guess the number between 1 and 20: "))
    
    if guess == random_number:
        print("You did it!")
    else:
        print(f" The correct number was {random_number}.")