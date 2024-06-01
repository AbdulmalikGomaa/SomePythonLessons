# import time                                 #O(1)
# array_size = 1000                           #O(1)
# test_array = list(range(array_size))        #O(1)
# target_element = array_size - 1             #O(1)
#
# start_time = time.time()                    #O(1)
# search(test_array, target_element)
# end_time = time.time()                      #O(1)
#
# execution_time = end_time - start_time      #O(1)
# #O(7)
#
#
# def search(arr, target):
#     for element in arr:                     #O(n)
#         if element == target:               #O(n)
#             return True                     #O(n)
#         return False                        #O(n)
#
#
#
#
# def get_first_element(arr):                 #O(n)
#     return arr[0]                           #O(n)

boxes = [1, 2, 3, 4, 5]

def printinpairs(arr):          #O(3n) = O(n)
    for i in arr:               #O(n)
        for v in arr:           #O(n)
            print(i, v)         #O(n)


printinpairs(boxes)
