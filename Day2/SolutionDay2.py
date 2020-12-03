def readFile(filename):
    fileObject = open(filename, "r")  # file is opened in read mode
    entries = fileObject.read().splitlines()  # puts the file content into array
    fileObject.close()
    return entries

inputFile = "inputDay2.txt"
passwordsList = readFile(inputFile)

validPasswords1 = 0
validPasswords2 = 0

for element in passwordsList: #solution to part 1 of the Day2 task
    counter = 0

    mainPart, password = element.split(":")
    occurences, letter = mainPart.split(" ")
    lowest, highest = occurences.split("-")

    for character in password:
        if character == letter:
            counter += 1

    if counter < int(lowest) or counter > int(highest): pass
    else:
        validPasswords1 += 1

    counter = 0

    if password[(int(lowest))-1] == letter and password[(int(highest)-1)] == letter:
        pass
    elif password[(int(lowest)-1)] == letter or password[(int(highest)-1)] == letter:
        validPasswords2 += 1

    # My code, but it was not working correctly
    # TO DO: debug and chek why it was not working
    # elif len(password) >= (int(highest)+1):
    #     if password[int(lowest)+1] == letter:
    #         counter += 1
    #     elif password[int(highest)] == letter:
    #         counter += 1


print(validPasswords1)
print(validPasswords2)

#Idea found on github
with open('inputDay2.txt') as file:
    counter = 0
    for line in file:
        c = 0
        data = line.strip().split(' ')
        data[0] = data[0].split('-')
        data[1] = data[1][0]
        try:
            if data[2][int(data[0][0]) - 1] == data[1] and data[2][int(data[0][1]) - 1] == data[1]:
                pass
            elif data[2][int(data[0][0]) - 1] == data[1] or data[2][int(data[0][1]) - 1] == data[1]:
                counter += 1
        except IndexError:
            pass

print(counter)
