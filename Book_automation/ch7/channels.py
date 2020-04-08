import re



#regexp can use channels - find Batman OR Wolverine
heroRegex = re.compile(r'Batman|Wolverine')

mo1 = heroRegex.search(' Robin and Batman return')
print(mo1.group())

# if both are presented, first match will be taken to mo2
mo2 = heroRegex.search('Wolverine is cool, and Batman suxx, ')
print(mo2.group())

# findall() is a method toregexp, finds all matches
mo3 = heroRegex.findall('Batman and robin can not kick ass to Wolverine')
print(mo3)

print('========use batRegex==============')
# if we try to find alter variants with common letters - bat-man, bat-girl, bat-mobile, bat-copter, etc, we use CHANNELS = '|' sign
batRegex = re.compile(r'Bat(man|girl|mobile|copter)')

bmo = batRegex.search('Batmobile is out of fuel')

#this prints all matching text
print(bmo.group())

#this prints first group, which is 'mobile'
print(bmo.group(1))

