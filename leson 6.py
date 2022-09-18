lits  = [1409, 4901, 1904, 9041, 4109]
lits2 = ["e", "ee", "eee", "eeee", "eeeee"]
print(lits)
print(lits2)
print(lits[1:3])
print(lits2[::2])
lits.append(lits2[1])
print(lits)
lits2.extend(lits)
print(lits2)
