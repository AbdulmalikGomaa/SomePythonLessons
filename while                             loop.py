#"route1"
aminals = ["parrot", "lion", "giraffe", "bobcat", "budgie"]
print("this is a list of aMMMMMMinals:")
print(aminals)
aminals.append(input("input extra 2...\n"))
aminals.append(input())
aminals.remove("parrot")
aminals.remove("budgie")
print("this is the list now:")
print(aminals)

#فاصل و نواصل

print("\n\n" + "░░▒▒▓▓██" * 50 + "\n\n") #فن

#و الان نواصل معكم

#"route2"
InteractiveListLol = []
print("You are asked to fill in a survey with 5 of your favorite genres in a certain category.")
Category = str(input("What category are you going to pick? \n"))

InputCount = 0
print("Please fill in...")
while InputCount != 5:
    InteractiveListLol.append(input())
    InputCount += 1
print("These are your favorite 5 things in " + Category + ". I know, I suck at my job (as a python beginner).")
print(InteractiveListLol)
