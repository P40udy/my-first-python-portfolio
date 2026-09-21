import random
seceret_number = random.randint(1, 25)
lives = 6
attempts = 1
print("this is your first attempt, you have 6 guesses to correctly guess the number between 1 and 25")
while lives > 0:
    number = int(input("what number do you guess?  "))
    if number == seceret_number:
        print("correct, you win")
        break
    elif number > seceret_number:
        print("too high")
        lives -= 1
        print("you are on ", lives, "lives")
    elif number < seceret_number:
        print("too low")
        lives -= 1
        print("you are on ", lives, "lives")
    if lives == 0:
        print("you failed")
        try_again = input("want to try again.  Yes  or  No?  ")
        if try_again == "yes":
            lives = 6
            attempts += 1
            print("this is your ", attempts, "nd attempt")
        elif try_again == "no":
            break
                