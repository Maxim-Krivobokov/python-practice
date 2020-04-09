import os

hellofile = open('test.txt')
# hellofile contents is type FILE

#this var will have all strings from file
content = hellofile.read()
hellofile.close()
print(content)

hellofile2 = open('strings.txt')
# readlines() method rerutns list of strings
print(hellofile2.readlines())

testfile = open('test.txt', 'w')

testfile.write('Hello world!\n')

testfile.close()

testfile = open('test.txt', 'a')

testfile.write(' id dont know wat to write')

testfile.close()

testfile = open('test.txt')
content1 = testfile.read()
testfile.close()
print(content1)
