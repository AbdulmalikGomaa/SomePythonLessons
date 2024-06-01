# def my_decorator(func):
#     def my_nested_function(n1, n2):
#         if n1 <= 0:
#             print("invalid")
#         else:
#             func(n1, n2)
#     return my_nested_function
#
# @my_decorator
# def division(n1,n2):
#     print(n1/n2)
#
# division(19, 6)

import time
def executiontime(func):
    def func2(t1, t2):
        print(f"the execution time was {t2-t1} seconds")
    return func2

@executiontime
def pr(t1, t2):
    t1 = time.time()*1000
    for i in range(124):
        print(i**i)
    t2 = time.time()*1000

pr(12, 12)
