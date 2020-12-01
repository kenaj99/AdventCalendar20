def readFile (filename):
    fileObject = open(filename, "r") #file is opened in read mode
    entries = fileObject.read().splitlines() #puts the file content into array
    fileObject.close()
    return entries
inputFile = "inputDay1.txt"

expensesArray = readFile(inputFile)
result = 0

for element in expensesArray:
    a = int(element)
    b = 2020 - a
    if str(b) in expensesArray:
        result = a * b
        
print(result)