set1 = {"insert", "set", "item"}
print(set1)
set2 = {"reinsert", "reset", "reitem"}
print(set2)
set1.update(set2)
print(set1)
set3 = set1.union(set2)
print(set3)
set4 = {"I hate the fact that you must already have an element in the set so you can add more"}
set4.add("h")
set4.add("g")
print(set4)
set5 = {"last", "set", "to", "go"}
set5.discard("can't believe how silly I am")
print(set5)
