from turtle import *

t = Turtle()

# def pen(n,l):
#     for i in range(n):
#         t.fd(l)
#         t.lt(360/n)
#
# t.color("red")
# t.begin_fill()
# pen(12, 100)
# t.end_fill()

# for i in range(3):
#     for v in range(5):
#         t.fd(100)
#         t.lt(72)
#     t.lt(120)
for i in range(200, -200, -10):
    t.fd(i)
    t.lt(120)
