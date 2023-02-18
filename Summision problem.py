List1 = [32, 65, 84, 14, 97, 52, 71]
AdditionVar = 0

# For loop method

for LoopThing in List1:
    AdditionVar += LoopThing
    print(AdditionVar)

print("_" * 70)

# While Loop method

AdditionVar = 0
LoopThing2 = 0  # Bcuz I don't understand what "can be undefined" mean

while LoopThing2 < len(List1):
    AdditionVar += List1[LoopThing2]
    print(AdditionVar)
    LoopThing2 += 1

print("_" * 70)
