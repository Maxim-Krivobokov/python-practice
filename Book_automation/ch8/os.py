import os

# we must add correct path symbols \ and / to make program work in Windows and Linux

# function adds special symbol \ or /, depending on current OS
print(os.path.join('usr', 'bin', 'spam'))

# this function is good for creating filepaths
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

print('creating correct filenames')
for filename in myFiles:
    print(os.path.join('C:\\Users\\Akakii', filename))

print('===============cwd=pwd========================')

# getcwd() is fuction to get current directiory path

curDir = os.getcwd()
print(os.getcwd())

# chdir() is function like cd

# os.chdir('C:\\Windows\\System32')
print(os.getcwd())

os.chdir(curDir)

print('===============makedirs========================')

# fucntion makedirs() is like mkdir
print('making local dir tempdir')
# os.makedirs('.\\tempdir')

print('======using os.path functions =================')

print(os.path.abspath('.'))

print(os.path.abspath('.\\tempdir'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\temp'))

path1 = 'C:\\Windows\\System32\\calc.exe'
print('--------dirname and basename ~filename---------')
print(os.path.basename(path1))
print(os.path.dirname(path1))


print('-----split function returns tuple --------')
# splits to dirname adn basename
print(os.path.split(path1))

# split to single dirs
print(path1.split(os.path.sep))
