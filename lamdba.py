def definition():
    global r
    r = int(input())
    return lambda: r+2

when = True

while when:
    print(definition())

