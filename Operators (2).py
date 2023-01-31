var1 = 47
#int --> float
print(float(var1))
#int --> complex
print(complex(var1))
#int --> string
print(str(var1))
print(type(str(var1)))
#float --> integer
var2 = 56.7
print(int(var2))
#float --> complex
print(complex(var2))
#float --> string
print(str(var2))
print(type(str(var2)))
#complex --> string
var3 = 27+0j
print(str(var3))
print(type(str(var3)))
#string --> integer
var4 = "92"
print(int(var4))
#string --> float
print(float(var4))
#string --> complex
print(complex(var4))

print("_"*70)

str1 = "strign"
tuple1 = ("t", "u", "p", "l", "e")
list1 = ["l", "i", "s", "t"]
set1 = {"s", "e", "t"}
dict1 = {"d": 1, "i": 1, "c": 1, "t": 1, }
#string --> tuple
print(tuple(str1))
#string --> list
print(list(str1))
#string --> set
print(set(str1))
#tuple --> string
print(str(tuple1))
#tuple --> list
print(list(tuple1))
#tuple --> set
print(set(tuple1))
#tuple --> dict
print(dict.fromkeys(tuple1))
#list --> string
