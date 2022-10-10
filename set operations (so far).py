print("_"*100+"\n"
             "I don't know where to start\n"
             ".union()")

q = {1, 3, 5, 7, 9}
w = {0, 2, 4, 6, 8}
print("\n\nThis is set Q")
print(q)
print("\nThis is set W")
print(w)
print("\nThis is set Q union set W")
print(q.union(w))

print("\n"+"_"*100+"\n"
             ".update()")

print("\n\nThis is set Q updated with set W, which is just like union except that it changes the set.")
q.update(w)
print(q)

print("\n"+"_"*100+
             "\n.remove()")

e = {"0_element", "1_element", "2_element", "3_element"}
print("\n\nThis is set E")
print(e)
print("\nThis is set E with \"3_element\" removed")
e.remove("3_element")
print(e)
print("\nThe element mentioned must be included in the set or it will give an error\n")

print("\n"+"_"*100+
             "\n.discard()")

print("\n\nThis is set E with \"2_element\" discarded")
e.discard("2_element")
print(e)
print("\nUnlike .remove(), .discard() doesn't give an error when discarding an element that isn't included in the set.")
e.discard("4_element")

print("\n"+"_"*100+
             "\n.add")

print("\n\nThis is set E after adding \"4_element\" and \"5_element\"")
e.add("4_element")
e.add("5_element")
print(e)
print("\nYou can only add 1 element each time you use .add() attribute. r/wellthatsucks")

print("\n"+"_"*100+
             "\n.copy()")

r = e.copy()
print("\n\nThis is set R, which is a copy of set E")
print(r)

print("\n"+"_"*100+
             "\n.clear()")

print("\n\nThis is set E after it was cleared")
e.clear()
print(e)

print("\n"+"_"*100+
             "\n.difference()")

t = {1, 2, 3}
y= {2, 3, 4, 5}
print("\n\nThis is set T")
print(t)
print("\nThis is set Y")
print(y)
print("\nThis is set T difference set Y")
print(t.difference(y))

print("\n"+"_"*100+
             "\n.difference_update()")

print("\n\nThis is set T difference set Y after set T is updated")
t.difference_update(y)
print(t)

print("\n"+"_"*100+
             "\n.intersection()")

u = {24, 55, 67}
i= {12, 67, 55, 43}
print("\n\nThis is set U")
print(u)
print("\nThis is set I")
print(i)
print("\nThis is set U intersection set I")
print(u.intersection(i))

print("\n"+"_"*100+
             "\n.intersection_update()")

print("\n\nThis is set U intersection set I after set U is updated")
u.intersection_update(i)
print(u)

print("\n"+"_"*100+
             "\n.symmetric_difference()")

o = {"I", "prefer", "numbers"}
p= {"prefer", "numbers", "on", "strings"}
print("\n\nThis is set O")
print(o)
print("\nThis is set P")
print(p)
print("\nThis is set O difference set P, except that the result is the different elements in both the sets.")
print(o.symmetric_difference(p))
print("I don't remember learning this one in school, but this is my understanding.")

print("\n"+"_"*100+
             "\n.symmetric_difference_update()")

print("\n\nIt's the same + update set")
o.symmetric_difference_update(p)
print(o)

print("\n"+"_"*100+
             "\n.issuperset()")

a = {14, 15, 16, 17, 18}
s = {15, 16, 17}
print("\n\nThis is set A")
print(a)
print("\nThis is set S")
print(s)
print("\nI don't know how to say these")
print("\nThis is the result of S being the \"superset\" of A:")
print(s.issuperset(a))
print("\nThis is the result of A being the \"superset\" of S:")
print(a.issuperset(s))
print("\nThat's from my understanding. I didn't take this one in school, too.")

print("\n"+"_"*100+
             "\n.issubset()")

print("\n\nThis is the result of S being subset of A:")
print(s.issubset(a))
print("\nThis is the result of A being the subset of S:")
print(a.issubset(s))

print("\n"+"_"*100+
             "\n.isdisjoint()")

print("\n\nThis is the result of S not having any elements of those in A:")
print(s.isdisjoint(a))
print("\nThis is the result of A not having any elements of those in S:")
print(a.isdisjoint(s))
print("\n\nThat is so far what I've learned in sets. It shouldn't take 161 lines to make every set operation of these but I just wanted to try and explain. I have no idea why.")


ecsit = input()
if ecsit != "":
    quit("you didn't have to say anything")
else:
    quit()
