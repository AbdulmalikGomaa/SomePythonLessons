from time import sleep

segment1 = "\\"
segment2 = "|"
segment3 = "/"
segment4 = "-"


def progressbar():
    print(f"\r{segment1}", end="")
    sleep(0.1)
    print(f"\r{segment2}", end="")
    sleep(0.1)
    print(f"\r{segment3}", end="")
    sleep(0.1)
    print(f"\r{segment4}", end="")
    sleep(0.1)
    progressbar()

progressbar()

#it was meant to be a progressbar but it failed.
