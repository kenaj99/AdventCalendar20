def readFile(filename):
    fileObject = open(filename, "r")  # file is opened in read mode
    entries = fileObject.read().split("\n\n")  # puts the file content into array dividing by empty line
    fileObject.close()
    return entries

"""
Passport fields:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID) - optional
cid (Country ID)
"""

validPassports = 0
inputFile = "inputDay4.txt"
passports = readFile(inputFile)

for person in passports:
    person = person.replace("\n", " ")
    counter = 0
    for character in person:
        if character == ":":
            counter += 1
    if "cid" not in person and counter == 7:
        validPassports += 1
    elif counter == 8:
        validPassports += 1

print(validPassports)
