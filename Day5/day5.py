import math

def readFile(filename):
    fileObject = open(filename, "r")  # file is opened in read mode
    entries = fileObject.read().splitlines()  # puts the file content into array
    fileObject.close()
    return entries


planeSeats = readFile("inputDay5.txt")

maxID = 0
#TO DO: debug and find out why it is not working correctly
for seat in planeSeats:
    rowStart = 0
    rowEnd = 127
    rowMiddle = 0
    columnStart = 0
    columnEnd = 7
    columnMiddle = 0
    counter = 0
    row = 0
    column = 0
    ID = 0
    for value in seat:
        if value == "B":
            rowMiddle = math.ceil((rowEnd-rowStart)/2)
            rowEnd -= rowMiddle
            if counter == 6:
                row = rowEnd
            counter += 1
        elif value == "F":
            rowMiddle = math.floor((rowEnd-rowStart)/2)
            rowStart += rowMiddle
            if counter == 6:
                row = rowStart
            counter += 1
        elif value == "R":
            columnMiddle = math.ceil((columnEnd-columnStart)/2)
            columnEnd -= columnMiddle
            if counter == 9:
                column = columnEnd
            counter += 1
        elif value == "L":
            columnMiddle = math.floor((columnEnd-columnStart)/2)
            columnStart += columnMiddle
            if counter == 9:
                column = columnStart
            counter += 1
        ID = row * 8 + column
        if ID > maxID:
            maxID = ID
    print(seat)

print(maxID)

# code found on github
# def seat_coord(input):
#     input = input.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
#     return int(input[0:7], 2), int(input[7::], 2)
#
#
# def seat_id(row, column):
#     return row * 8 + column
#
# with open('inputDay5.txt') as file:
#     tab = []
#     for line in file:
#         tab.append(line.strip())
# highest_id = 0
#
#
# id_tab = []
#
# for t in tab:
#     row, column = seat_coord(t)
#     id_tab.append(seat_id(row, column))
# print(max(id_tab))