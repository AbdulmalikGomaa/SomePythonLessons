#difference
ThisIsSet1 = {"yes", 1, 2, 3, 4, 5}
ThisIsSet2 = {"it", "is", 3, 4, 5, 6, 7}
print(ThisIsSet1)
print(ThisIsSet2)
print(ThisIsSet1.difference(ThisIsSet2))
print(ThisIsSet1 - ThisIsSet2)
#difference_update
ThisIsSet1.difference_update(ThisIsSet2)
print(ThisIsSet1)
#intersection
ThisIsSet3 = {"no", 24, 26, 29}
ThisIsSet4 = {"way", 26}
print(ThisIsSet3)
print(ThisIsSet4)
print(ThisIsSet3.intersection(ThisIsSet4))
print(ThisIsSet3 & ThisIsSet4)
#intersection_update
ThisIsSet3.intersection_update(ThisIsSet4)
print(ThisIsSet3)
#symmetric_difference
ThisIsSet5 = {"W", "A", "R", "I", "O", "O", "O"}
ThisIsSet6 = {"W", "A", "L", "U", "I", "G", "I", "I", "I"}
print(ThisIsSet5)
print(ThisIsSet6)
print(ThisIsSet5.symmetric_difference(ThisIsSet6))
print(ThisIsSet5 ^ ThisIsSet6)
#symmetric_difference_update
ThisIsSet5.symmetric_difference_update(ThisIsSet6)
print(ThisIsSet5)
#I don't know what exactly is {'O', 'L', 'U', 'G', 'R'}
