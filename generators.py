# def cube_of_n(n):
#     for i in range(1, n+1):
#         yield i**3
# gen = cube_of_n(int(input("enter a number   ")))
#
# for i in gen:
#     print(i)

# def fibonacci(n):
#     yield 0
#     yield 1
#     for i in range(1, n):
#
# gen = fibonacci(int(input("enter a number   ")))
# for x in gen:
#     print(x)

def factorial(n):
    for i in range(1, n+1):
        if i == 1:
            n2 = i
        else:
            n2 *= i
    yield n2

gen = factorial(int(input("enter a number   ")))
for x in gen:
    print(x)
