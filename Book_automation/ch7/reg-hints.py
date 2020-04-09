import re

print(r"======== unnecessarry patterns (xyz)? ==============")
# this means that (wo) is unnecessarry. Batman or Batwoman will both match
batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('Adventures of Batman')

print(mo1.group())

mo2 = batRegex.search('Adventures of Batwoman')

print(mo2.group())

print('=========multiple matches with * (0->N)========================')

# wo can be used from 0 to N times. batman, batwoman, batwowoman - all match
babatRegex = re.compile(r'Bat(wo)*man')

mo4 = babatRegex.search('Adventures of Batman')

print(mo4.group())

mo5 = babatRegex.search('Adventures of Batwoman')

print(mo5.group())

mo6 = babatRegex.search('Adventures of Batwowowoman')

print(mo6.group())


print('=========multiple matches with + (1->N)========================')

# wo can be used from 0 to N times. batman, batwoman, batwowoman - all match
batttRegex = re.compile(r'Bat(wo)+man')

mo4 = batttRegex.search('Adventures of Batman')
print('is mo4 equal to None?')
print(mo4 == None)

mo55 = batttRegex.search('Adventures of Batwoman')

print(mo55.group())

mo66 = batttRegex.search('Adventures of Batwowowoman')

print(mo66.group())



print('==========dealing with phone numbers============')
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

ph01 = phoneRegex.search('My number is 415-555-3232')

print(ph01.group())

ph02 = phoneRegex.search(' my short number is 999-7575')

print(ph02.group())

# method FINDALL

phoneRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # no groups

phoneRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # 3 groups

print('=====================================================')
print('My number is 123-345-5678, worknum is 994-131-4627')
#output will be list of strings
print('no-group findall:')
print(phoneRegex1.findall('My number is 123-345-5678, worknum is 994-131-4627'))

#output will be list of tuples
print(' findall with groups:')
print(phoneRegex2.findall('My number is 123-345-5678, worknum is 994-131-4627'))




# symbol classes
# \d = [0-9] \s = [' '|\t|\n] \w = [a-z, 0-9, _]
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies'))

