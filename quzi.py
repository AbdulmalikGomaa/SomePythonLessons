# 1- bool_variable = True
# 2- type()
# 3- int()
# 4- 11.0
# 5-
held = None
attended = None
percentage = None

while True:
    try:
        held = int(input("Enter the number of held classes: "))
    except ValueError:
        print("Entered value couldn't be converted to an integer.")
        continue
    try:
        attended = int(input("Enter the number of attended classes: "))
    except ValueError:
        print("Entered value couldn't be converted to an integer.")
        continue
    percentage = held/attended
    if percentage < 0.75:
        print(f"You got {percentage*100}%, and failed.")
    elif percentage > 0.75:
        print(f"You got {percentage*100}%, and succeeded.")
# 6-
var1 = None

while var1 != 22:
    if var1 == None:
        var1 = 2
        print(var1*2)
        continue
    print(var1*2)
    var1 += 2
# 7-
import random

guess = None
attemptCounter = 0


while True:
    var1 = random.randint(1, 100)
    print("I've chosen a number from 1 to 100, can you guess what it is?")
    while guess != var1:
        try:
            guess = int(input())
        except guess % 1 > 0 or ValueError:
            print("Please enter an integer.")
            continue
        if guess > var1:
            print("That is incorrect! Guess lower.")
            attemptCounter += 1
            continue
        elif guess < var1:
            print("That is incorrect! Guess higher.")
            attemptCounter += 1
            continue
        elif guess == var1:
            print(f"That is correct! It took you {attemptCounter} attempts.")