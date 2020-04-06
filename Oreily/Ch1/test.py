from os import getcwd
import sys
import time

path1 = getcwd()

str2 = sys.platform
print( path1 )

print (str2)



today = time.strftime( "%A" )

if today == 'Thursday':
    print ('4etverg')
elif today == 'Saturday':
    print ('subbota')
else:
    print ('other day')
    print (today)