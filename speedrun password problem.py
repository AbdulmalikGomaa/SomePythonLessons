Password = "244466666"
RemainingAttempts = 3
UserInput = str(input("Password: "))
while UserInput != Password:
    RemainingAttempts -= 1
    print("Wrong password. " + str(RemainingAttempts) + " attempts remaining.")
    if RemainingAttempts == 0:
        break
    UserInput = str(input("Password: "))
else:
    print(" يا فرحة" * 50)
    # the teacher told us to make a login thing one day. that's all about it.
