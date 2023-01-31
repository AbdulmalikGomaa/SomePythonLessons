lis_t = [1, 2, 3, 5]
var1 = lis_t[0]
missingElement = 0
if lis_t[1] - var1 == 2:
    missingElement = var1 + 1
    print(missingElement)
else:
    var1 = lis_t[1]
if lis_t[2] - var1 == 2:
    missingElement = var1 + 1
    print(missingElement)
else:
    var1 = lis_t[2]
if lis_t[3] - var1 == 2:
    missingElement = var1 + 1
    print(missingElement)
else:
    var1 = lis_t[4]


