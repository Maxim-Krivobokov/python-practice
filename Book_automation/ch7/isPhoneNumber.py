

# this function checks, is the text == telephone number (XXX-XXX-XXXX) ? or not and returns True or False
# this funct DO NOT use REGEXP
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('telephone number format is 123-456-7890')
testnum = input('Enter a telephone number \n')
print(isPhoneNumber(testnum))
