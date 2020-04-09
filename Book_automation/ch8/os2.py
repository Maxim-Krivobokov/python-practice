import os

#os.path.getsize() returnsd size
print(os.path.getsize('C:\\Windows\\System32\\Calc.exe'))

print(os.listdir('C:\\'))

print('---counting size of system32 files-----')

totalsize = 0

#getting list of files (ls) in system32 folder
for filename in os.listdir('C:\\Windows\\System32'):
    totalsize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename)) #call getsize function for all file, after creating full path for it with join()

print('size is ' + str(totalsize) + ' bytes')

# different fucntions

print('============checking existance==============')
print(os.path.exists('C:\\Windows'))

print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))

print(os.path.isdir('C:\\temp'))