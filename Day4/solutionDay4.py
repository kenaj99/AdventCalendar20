# def readFile(filename):
#     file_object = open(filename, "r")  # file is opened in read mode
#     entries = file_object.read().split("\n\n")  # puts the file content into array dividing by empty line
#     file_object.close()
#     return entries
#
# """
# Passport fields:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID) - optional
# cid (Country ID)
# """
#
# validPassports1 = 0
# validPassports2 = 0
#
# inputFile = "inputDay4.txt"
# passports = readFile(inputFile)
#
# #TO DO! - it's still not working debugging is needed
#
# for person in passports:
#     person = person.replace("\n", " ")
#     counter = 0
#     validField = 0
#     for character in person:
#         if character == ":":
#             counter += 1
#     if "cid" not in person and counter == 7:
#         validPassports1 += 1
#     elif counter == 8:
#         validPassports1 += 1
#     else:
#         person = "SKIP"
#     person = person.split(" ")
#     for field in person:
#         field = field.split(":")
#         if field[0] == "byr":
#             if 1920 <= int(field[1]) <= 2002:
#                 validField += 1
#         if field[0] == "iyr":
#             if 2010 <= int(field[1]) <= 2020:
#                 validField += 1
#         if field[0] == "eyr":
#             if 2020 <= int(field[1]) <= 2030:
#                 validField += 1
#         if field[0] == "hgt":
#             length = len(field[1])
#             if "cm" in field[1]:
#                 if 150 <= int(field[1][0:length-2]) <= 193:
#                     validField += 1
#             if "in" in field[1]:
#                 if 59 <= int(field[1][0:length-2]) <= 76:
#                     validField += 1
#         if field[0] == "hcl":
#             if len(field[1]) == 6:
#                 validField += 1
#         if field[0] == "pid":
#             if len(field[1]) == 9:
#                 validField += 1
#         if field[0] == "ecl":
#             string = "amb blu brn gry grn hzl oth"
#             if field[1] in string:
#                 validField += 1
#     if validField == 7:
#         validPassports2 += 1
#
# print("First validation: " + str(validPassports1))
# print("Second validation: " + str(validPassports2))
#
# """
# Second validation
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# """

#code found on github
def extract_documents(tab): #very good function to save data from input file as a dictionary
    documents = []
    document = {}
    for line in tab:
        if line:
            values = line.split(' ')
            for value in values:
                v = value.split(':')
                document[v[0]] = v[1]
        else:
            documents.append(document)
            document = {}
    documents.append(document)

    return documents


def check_fields(document, required_fields):
    for field in required_fields:
        try:
            document[field]
        except KeyError:
            return False
    return True


with open('inputDay4.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def validate_document(document):
    if 1920 < int(document['byr']) < 2002:
        pass
    else:
        return False

    if 2010 <= int(document['iyr']) <= 2020:
        pass
    else:
        return False

    if 2020 <= int(document['eyr']) <= 2030:
        pass
    else:
        return False

    if document['hgt'][-2:-1] == 'cm':
        hgt = list(document['hgt'])
        hgt.pop()
        hgt.pop()
        if 150 < int(hgt) < 193:
            pass
        else:
            return False

    if document['hgt'][-2:-1] == 'in':
        hgt = list(document['hgt'])
        hgt.pop()
        hgt.pop()
        if 59 < int(hgt) < 76:
            pass
        else:
            return False

    if document['hcl'][0] == '#':
        for character in document['hcl'][1:-1]:
            if character not in '0123456789abcdef':
                return False
    else:
        return False

    if document['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        pass
    else:
        return False

    if len(document['pid']) == 9:
        pass
    else:
        return False

    return True


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
documents = extract_documents(tab)
counter = 0
for document in documents:
    if check_fields(document, required_fields):
        if validate_document(document):
            counter += 1
print(counter)


