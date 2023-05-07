# import math
# import numpy as np
# from time import sleep
#
#
# print("                 _____BETA VERSION 1.0_____                 \n"
#       "Thanks for testing the beta version of this useless calculator project.\n"
#       "I don't expect this to get much updates, as this is just homework, or you can say additional work.\n"
#       "Don't expect much potential from this, as I'm still a 9th grader and I still don't know much xd\n\n"
#       "Enter /help or /? for how to use and /log or /! for changelog.\n")
#
# FirstInputBackup = 0
# SecondInput = 0
# RootedNumberQuestionMark = 0
#
# FirstInput = (input())
# while FirstInput != "/exit" or FirstInput != "/0":
#       #Changelog section:
#       if FirstInput == "/log" or FirstInput == "/!":
#             print("             __Version: 1.0, nothing much__             \n\n"
#                   "- Operators, of course (+, -, *, /, %, sqrt, cbrt)\n")
#       #Help section:
#       elif FirstInput == "/help" or FirstInput == "/?":
#             print("Enter numbers alone and operators (signs) alone in order. Yes, that's all.\n"
#                   "For square root and cube root, enter sqrt_ and cbrt_ before the number.\n"
#                   "Enter /submit or /= when you're done.\n"
#                   "Power function is still wip so you can't use it.")
#       #Some operators' section:
#       elif FirstInput == "+":
#             SecondInput = input()
#             FirstInputBackup = float(FirstInputBackup) + float(SecondInput)
#       elif FirstInput == "-":
#             SecondInput = input()
#             FirstInputBackup = float(FirstInputBackup) - float(SecondInput)
#       elif FirstInput == "*":
#             SecondInput = input()
#             FirstInputBackup = float(FirstInputBackup) * float(SecondInput)
#       elif FirstInput == "/":
#             SecondInput = input()
#             FirstInputBackup = float(FirstInputBackup) / float(SecondInput)
#       elif FirstInput == "%":
#             SecondInput = input()
#             FirstInputBackup = float(FirstInputBackup) % float(SecondInput)
#       elif "sqrt_" in FirstInput:
#             RootedNumberQuestionMark = math.sqrt(float(FirstInput.replace("sqrt_", "")))
#             FirstInputBackup = RootedNumberQuestionMark
#       elif "cbrt_" in FirstInput:
#             RootedNumberQuestionMark = np.cbrt(float(FirstInput.replace("cbrt_", "")))
#             FirstInputBackup = RootedNumberQuestionMark
#       #Resulting section or whatevr:
#       elif FirstInput == "/submit" or FirstInput == "/=":
#             print(FirstInputBackup)
#             FirstInputBackup = 0
#       #Exitting section:
#       elif FirstInput == "/exit" or FirstInput == "/0":
#             quit()
#       #Any other input crap section:
#       else:
#             FirstInputBackup = FirstInput
#
#
#
#
#       FirstInput = (input())
#

var1 = 0
var2 = 0
operation = 0


print("Enter /exit to exit and /reset to reset calculation.")

def addition():
    try:
        result = float(var1)+float(var2)
    except ValueError:
        print("One or both of the values you entered could not be converted to a float.")
    else:
        print(result) if float(result) != int(result) else print(int(result))

def subtraction():
    try:
        result = float(var1)-float(var2)
    except ValueError:
        print("One of the values you entered could not be converted to a float.")
    else:
        print(result) if float(result) != int(result) else print(int(result))

def multiplication():
    try:
        result = float(var1)*float(var2)
    except ValueError:
        print("One of the values you entered could not be converted to a float.")
    else:
        print(result) if float(result) != int(result) else print(int(result))

def division():
    try:
        result = float(var1)/float(var2)
    except ValueError:
        print("One of the values you entered could not be converted to a float.")
    else:
        print(result) if float(result) != int(result) else print(int(result))

def calculation():

    operation = str(input("Enter operation (+, -, *, /): "))

    if operation == "+":
        addition()

    elif operation == "-":
        subtraction()

    elif operation == "*":
        multiplication()

    elif operation == "/":
        division()

    elif operation == "/reset":
        pass

    else:
        print("Specified operation is not included.")
        calculation()

while var1 != "/exit" or var2 != "/exit" or operation != "/exit":

    var1 = input("Enter first number: ")

    if var1 == "/reset":
        print("Like why would you do that")
        continue

    var2 = input("Enter second number: ")

    if var2 == "/reset":
        continue

    calculation()

quit()
