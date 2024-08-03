ls1 = [1, 2, 3, 5, 9]


def funct(ls, target):
    lp = 0
    rp = -1
    while ls[lp] + ls[rp] != target:
        print(ls[lp], ls[rp])
        if ls[rp] >= target:
            rp -= 1
        else:
            if ls[rp] >= ls[lp]:
                lp += 1
    return True

print(funct(ls1, 8))

