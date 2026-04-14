import random
import string
l = int(input("Enter password length : "))
ch = f"{string.ascii_letters}{string.digits}"
password = ''.join(random.choice(ch) for i in range(l))
print("Your password is :", password)