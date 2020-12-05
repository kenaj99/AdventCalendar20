def readFile(filename):
    fileObject = open(filename, "r")  # file is opened in read mode
    entries = fileObject.read().split("\n\n")  # puts the file content into array dividing by empty line
    fileObject.close()
    return entries

passports = []
counter = 0
inputFile = "inputDay4.txt"
passports = readFile(inputFile)

print(passports)