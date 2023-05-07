from time import sleep

def defmorelikedeaf(*theparameter):
    for theiterator in theparameter:
        print(theiterator, end=" 0 ")
        sleep(0.1)
defmorelikedeaf("0", "0", "0", "0", "0", "0", "0", "0")

def deafthereturn(**thedict):
    for thekey, thevalue in thedict:
        print(f"Hello {thekey} from {thevalue}")
        sleep(0.1)
deafthereturn("Who", "am", "I", "?", " ", "Guess", "I\'ll", "never", "know", ".")
