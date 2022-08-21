import math
import numpy as np
from time import sleep

#first_name = input("first name goes here: ")
#sleep(0.25)
#second_name = input("second name goes here: ")
#sleep(0.25)
#age = input("age: ")
#sleep(0.25)
#print("so your name is " + first_name + " " + second_name + ", and you're " + str(age) + " years old. now leave.")
#sleep(5)
#print("self destruction in 5 seconds")
#sleep(5)
#quit()

# that was in the session, moving on to the the homework...

print("                 _____BETA VERSION 1.0_____                 \n"
      "Thanks for testing the beta version of this useless calculator project.\n"
      "I don't expect this to get much updates, as this is just homework, or you can say additional work.\n"
      "Don't expect much potential from this, as I'm still a 9th grader and I still don't know much xd\n\n"
      "Enter /help or /? for how to use and /log or /! for changelog.\n")

FirstInputBackup = 0
SecondInput = 0
RootedNumberQuestionMark = 0

FirstInput = (input())
while FirstInput != "/exit" or FirstInput != "/0":
      #Changelog section:
      if FirstInput == "/log" or FirstInput == "/!":
            print("             __Version: 1.0, nothing much__             \n\n"
                  "- Operators, of course (+, -, *, /, %, sqrt, cbrt)\n")
      #Help section:
      elif FirstInput == "/help" or FirstInput == "/?":
            print("Enter numbers alone and operators (signs) alone in order. Yes, that's all.\n"
                  "For square root and cube root, enter sqrt_ and cbrt_ before the number.\n"
                  "Enter /submit or /= when you're done.\n"
                  "Power function is still wip so you can't use it.")
      #Some operators' section:
      elif FirstInput == "+":
            SecondInput = input()
            FirstInputBackup = float(FirstInputBackup) + float(SecondInput)
      elif FirstInput == "-":
            SecondInput = input()
            FirstInputBackup = float(FirstInputBackup) - float(SecondInput)
      elif FirstInput == "*":
            SecondInput = input()
            FirstInputBackup = float(FirstInputBackup) * float(SecondInput)
      elif FirstInput == "/":
            SecondInput = input()
            FirstInputBackup = float(FirstInputBackup) / float(SecondInput)
      elif FirstInput == "%":
            SecondInput = input()
            FirstInputBackup = float(FirstInputBackup) % float(SecondInput)
      elif "sqrt_" in FirstInput:
            RootedNumberQuestionMark = math.sqrt(float(FirstInput.replace("sqrt_", "")))
            FirstInputBackup = RootedNumberQuestionMark
      elif "cbrt_" in FirstInput:
            RootedNumberQuestionMark = np.cbrt(float(FirstInput.replace("cbrt_", "")))
            FirstInputBackup = RootedNumberQuestionMark
      #Resulting section or whatevr:
      elif FirstInput == "/submit" or FirstInput == "/=":
            print(FirstInputBackup)
            FirstInputBackup = 0
      #Exitting section:
      elif FirstInput == "/exit" or FirstInput == "/0":
            quit()
      #Any other input crap section:
      else:
            FirstInputBackup = FirstInput




      FirstInput = (input())
