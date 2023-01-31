dict1 = {"Key1": "PlaceHolder1", "Key2": "PlaceHolder2", "Key3": "PlaceHolder3", "Key4": {"PlaceHolder1": "How come?"}}
print(dict1)
print("_"*70)
#.keys()
print(dict1.keys())
#.values()
print(dict1.values())
print("_"*70)
#Update
dict1["Key4"].update({"PlaceHolder2": "Something feels off..."})
dict1["Key5"] = "PlaceHolder5"
dict1["Key4"]["PlaceHolder3"] = "No, seriously."
print(dict1)
print("_"*70)
#copy()
IStoleDict1 = dict1.copy()
print(IStoleDict1)
print("_"*70)
#clear()
dict1.clear()
print(dict1)
print("_"*70)
#popItem()
PlzDonateMePoor = IStoleDict1.popitem()
print(PlzDonateMePoor)
print(IStoleDict1)
#Notice that it took only the last key defined in the dictionary, and removed it
print("_"*70)
#setDefault()
IStoleDict1.setdefault("Key5", "PlaceHolder5")
print(IStoleDict1)
print("_"*70)
#.items()
print(IStoleDict1.items())
print("_"*70)
#There still remains fromKeys(), which I forgot what it was

