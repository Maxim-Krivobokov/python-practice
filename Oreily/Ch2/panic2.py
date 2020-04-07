#! python3
# wemust convert this phrase to "on tap"
phrase = "Don't panic!"

plist = list(phrase)

print(phrase)
print(plist)


##
plist2 = []
plist2.extend(plist[1:3])
plist2.extend(plist[5:3:-1])
plist2.extend(plist[7:5:-1])
##


new_phrase = ''.join(plist2)
print(plist2)
print(new_phrase)
