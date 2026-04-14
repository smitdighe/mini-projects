import random
while True:
    print("You rolled:", random.randint(1,6))
    choice = input("Roll again? (yes/no): ")
    if choice.lower() != 'yes':
        break