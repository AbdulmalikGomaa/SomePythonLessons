var1 = 17
var2 = 49
var3 = "Here comes the question: what do I enter here?"
var4 = "vnbvbnbvbnbvbnbvbnbvbnb"
#Comparison and boolean operators
print(var1 >= var2)
print(var1 < var2 and len(var3) != len(var4))  #Must all be true, otherwise it will output false. Even if only one is true, it will output the same.
print(var1 < var2 or len(var4) > len(var3))  #Picks true out of them. If none, it will output false.
print(not len(var4) > len(var3))  #The opposite of the result. Nothing too confusing, I assume
#Arithmetic and assignment operators:
var5 = 11
var5 += var2  #var5 = var5 + var2
print(var5)
var1 -= var5  #var1 = var1 - var5
print(var1)

print(var1 % var5)
print(var2 / var1)
