import random
n = random.randint(1, 50)
guess = int(input("Guess number (1-50): "))
while guess != n:
    print("Too high!" if guess > n else "Too low!")
    guess = int(input("Try again: "))
print("You won!")