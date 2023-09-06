# map()
# It's a function used to apply a specified function to each item in an iterable, and then contains all the outcomes so that they are accessible by a for loop

# def hello(var):
#     return f"hello, {var}"
# collection = ["7ad 1", "7ad 2", "7ad 3"]
# thething = map(hello, collection)
#
# for i in thething:
#     print(i)
#     print("loop iteration end")

# assignment:
listofnumbers = [12321, 3215, 765, 16524, 762352, 7835642332, 75446475]
for i in map(lambda v: v*2, listofnumbers):
    print(i)
print("*"*round(69.420))
for i in filter(lambda x: x%2==0, [3562563434564345634563654,376,547,62453432,654265437,654378,562376,56436,5436,65436543654365436543,65436543654,3765387,2354325423,5476,4587,64987,589764,86790,8750,899,0,87,60897,60896,8576,8765,6475,4245,3256,4326,54,26534]):
    print(i)
print("*"*round(69.420))

