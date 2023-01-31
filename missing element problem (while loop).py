lisst = [12, 34, 78]

occupier1 = 0
occupier2 = occupier1 + 1
while lisst[occupier2] - lisst[occupier1] == 22:
    occupier1 += 1
else:
    lisst.insert(occupier2, lisst[occupier1] + 22)
    print(lisst[occupier2])
