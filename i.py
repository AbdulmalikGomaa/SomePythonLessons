import time
listofnames = [4654,6,543,64,365,436,5436543,65,43,6543,65,4364,365436,5436,54,73,65376,54,765,74,65746,547,6547,65,76,574,6547,654,7,63,4,325,432,54,26,54,36,53,65,437,653,7563,65,436,543,65,437,6,537,653,76,57,65,37,5636,54,365,436,54,3654,26,543,654,26,425,432,65,4376,54,765,48653,76,547,6537,6536,543,6543,65436543,6543,654365436,5437,56756,75637,2543,5242,6547365,376538,76538653,7542,42654,7365487653,6543,765378,653757365,37653,7865376,5376,53765,37653,765376,537653,7537,"nemo"]


def findnemo(arr):
    for i in arr:
        if i == "nemo":
            print("found")

starttime = time.time()
print(starttime)
findnemo(listofnames*1000000)
endtime = time.time()
print(endtime)
print(endtime - starttime)
time.sleep(32)
