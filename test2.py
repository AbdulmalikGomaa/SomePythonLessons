from time import sleep

segment_occupied = "█"
segment_unoccupied = " "

spreadsheet1 = "111111111111111111111111111111111111111111111111nl" \
               "110000000000000000000000000000000000000000000011nl" \
               "110000000000000000000001110000000000000000000011nl" \
               "110000000000000110000000111000000000000000000011nl" \
               "110000001100000000011000111000000000000000000011nl" \
               "110000000000000000110000111111110000000000000011nl" \
               "110001110000000001100000111111111000000000000011nl" \
               "110000011000001110000000111111111000000000000011nl" \
               "110000001111110000000000111111111100000000000011nl" \
               "110000000000000000000000011111111100000000000011nl" \
               "110000000000000000000000000000000000000000000011nl" \
               "110000000000000000000000000000000000000000000011nl" \
               "110000011100000000000000000000000000000000000011nl" \
               "110000100000000000000011110000001111000000000011nl" \
               "110000011110010001100100001000010001000000000011nl" \
               "110000000001010101000011110110001111000000000011nl" \
               "110000001110001010000000000000100001000001000011nl" \
               "110000000000000000000000000000011110000000000011nl" \
               "110000000000000000000000000000000000000000000011nl" \
               "111111111111111111111111111111111111111111111111"

def nothing_cursor():

    segment1 = "\\"
    segment2 = "|"
    segment3 = "/"
    segment4 = "-"

    for segment in segment1, segment2, segment3, segment4:
        print(f"{segment}\r", end="")
        sleep(0.05)
    nothing_cursor()



def spreadsheetprinter(spreadsheet):
    for iterator in spreadsheet:
        if iterator == "0":
            if spreadsheet.index(iterator) <= len(spreadsheet)-1:
                print(segment_unoccupied, end="")
                sleep(0.01)
            else:
                print(segment_unoccupied)
        elif iterator == "1":
            if spreadsheet.index(iterator) <= len(spreadsheet)-1:
                print(segment_occupied, end="")
                sleep(0.01)
            else:
                print(segment_occupied)
        elif iterator == "n":
            if spreadsheet[spreadsheet.index(iterator)+1] == "l":
                print("")
            else:
                print("\n There was an error reading the spreadsheet. There might have been an unsupported character in it.")
                break
        elif iterator == "l":
            pass
        else:
            print("\n There was an error reading the spreadsheet. There might have been an unsupported character in it.")
            break
    print("\n", end="")
    nothing_cursor()

spreadsheetprinter(spreadsheet1)


