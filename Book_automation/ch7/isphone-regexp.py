import re

#function to search phone numbers in text using regexp
def tlf_regexp_test(teststring):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    #phinenumregex is type regex now
    mo = phoneNumRegex.search(teststring)
    # calling search() method will assign match  object to mo variable
    print('Found number: ' + mo.group())
    #mo type has method group() that rerurns matching strings
    return mo.group()



def tlf_regexp_groups(teststring):
    # regular expressions is divided in groups
    # first group is (\d\d\d) , second (\d\d\d-\d\d\d\d)
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phoneNumRegex.search(teststring)

    #we can print different groups of object Match
    print('group 1: ' + mo.group(1))
    print('group 2: ' + mo.group(2))
    print('all groups : ' + mo.group(0))
    return mo.group()

print('single:')
tlf_regexp_test('My phone number is 123-555-0987')
print('groups:')
tlf_regexp_groups('My phone number is 543-765-8877')