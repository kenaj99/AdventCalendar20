def readFile(filename):
    fileObject = open(filename, "r")  # file is opened in read mode
    entries = fileObject.read().splitlines()  # puts the file content into array
    fileObject.close()
    return entries


inputFile = "inputDay1.txt"

expensesArray = readFile(inputFile)
result1 = 0

for element in expensesArray:
    a = int(element)
    b = 2020 - a
    if str(b) in expensesArray:
        result1 = a * b

print("Result 1: " + str(result1))

for element in expensesArray:
    for secondElement in expensesArray:
        a = int(element)
        b = int(secondElement)
        if a + b < 2020:
            c = 2020 - (a + b)
            if str(c) in expensesArray:
                result2 = a * b * c

print("Result 2: " + str(result2))

