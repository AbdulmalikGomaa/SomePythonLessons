def thing(x):
    if x-1 == 1:
        print(f"x-1 = {x}-1 = {x-1}\n"
              f"adding {x-1} to the previous value of x\n"
              f"total of numbers from first value of x to 1 = ", end="")
        return x+1
    print(f"x = {x}\nx+x-1 = {x}+{x-1} = {x+x-1}\n"
          f"adding {x+x-1} to the previous value of x")
    return x + thing(x-1)


while True:
    print(thing(int(input())))



#
# A simple interpretation of how the code works:
#
# -All the functions that are called are 1 function calling functions in itself.
# -The function returns the value of the argument, rather than the variable, that is added to what's returned from the function called after it.
# -The format of the equation after all values are returned is: x1 + x2 + x3 etc., with every x being the value returned in each end and every x after the one before is what the function has returned.
# -The last value outputted by a function is 2, and therefore the one after it is 1, so, to finish the recursion, it returns 1 instead of another function.
#
