import shutil
import time

width, height = shutil.get_terminal_size()
nl = "\n"
grnd = "█" * width
thirdgrnd = "█" * (round(1/3) * width)
twothirdsgrnd = "█" * (width - len(thirdgrnd) - 1)
weirdcharacter = "▒"

print(nl * round(2/3 * height))

print(thirdgrnd, end = "")
print(weirdcharacter, end = "")
print(twothirdsgrnd)

print((grnd + nl) * (round(1/3 * height) - 1))

time.sleep(55555)
