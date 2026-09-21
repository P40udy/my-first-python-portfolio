import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$"
print("welcome to a password generator and strength tester")
length = int(input("how long do you want your password to be: "))
password = ""
for i in range(length):
    password += random.choice(characters)
    print(password)

if length < 6:
    print("password is too weak")
elif length <= 12:
    print("not quite strong enough")
else:
    print("this password is strong enough")