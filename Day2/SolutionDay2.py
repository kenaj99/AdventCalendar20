def readFile(filename):
    fileObject = open(filename, "r")  # file is opened in read mode
    entries = fileObject.read().splitlines()  # puts the file content into array
    fileObject.close()
    return entries

inputFile = "inputDay2.txt"
passwordsList = readFile(inputFile)

validPasswords = 0

for element in passwordsList:
    counter = 0

    mainPart, password = element.split(":")
    occurences, letter = mainPart.split(" ")
    lowest, highest = occurences.split("-")

    for character in password:
        if character == letter:
            counter += 1

    if counter < int(lowest) or counter > int(highest): continue
    else:
        validPasswords += 1

print(validPasswords)
