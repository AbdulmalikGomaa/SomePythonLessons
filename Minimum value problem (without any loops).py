list1 = [1, 5, 3, 9, 13]
minimumValue = list1[4]
if minimumValue > list1[3]:
    minimumValue = list1[3]
if minimumValue > list1[2]:
    minimumValue = list1[2]
if minimumValue > list1[1]:
    minimumValue = list1[1]
if minimumValue > list1[0]:
    minimumValue = list1[0]
print(minimumValue)
