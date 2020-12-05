# with open('inputDay3.txt') as file: #Better implementation of file reading, found on GitHub
#     forest = []
#     for line in file:
#         forest.append(list(line.strip()))
#
# moveX = 3
# moveY = 1
# startPoint = [0, 0]
# currentPoint = startPoint
# trees = 0
#
# for row in forest:
#     length = len(row)
#     if currentPoint[0] <= (len(row)-3) and currentPoint[1] <= (len(forest)-1):
#         currentPoint[0] += moveX
#         currentPoint[1] += moveY
#         try:                                              #TO DO! deal with the error! it should work then
#             if forest[currentPoint[0]][currentPoint[1]] == "#":
#                 trees += 1
#         except IndexError:
#             continue
#     else:
#         bufferX = len(row) - currentPoint[0]
#         currentPoint[0] = (bufferX - 1)
#         currentPoint[1] += 1
#
# print(trees)

#easier way to deal with traversing through multiple "forests" found on github
with open('inputDay3.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))

slope = [1, 3]

multiplier = 1 + len(tab)/len(tab[0]) * (slope[1] / slope[0])
multiplier = int(multiplier) + 1
for i in range(0, len(tab)):
    tab[i] = tab[i] * multiplier

print(tab)

error = False
x = 0
y = 0
counter = 0
while not error:
    try:
        if tab[y][x] == '#':
            counter += 1
    except IndexError:
        error = True
    x += 3
    y += 1
print(counter)

