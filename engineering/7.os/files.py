def main():
    with open('file.txt', 'r+') as my_file:
        for i in range(20):
            my_file.write(f"test {i} \n")
        my_file.flush()  # delete all buffer. Readline or read will return nothing
        print(my_file.readline())# empty string
        print((type(my_file.readline()))) # string
        print('-' * 50)
        print(my_file.readlines()) # array of 20 lines
        print(type(my_file.readlines()))  # list
        print('-' * 50)
        print(my_file.read()) # empty
        print(type(my_file.read()))  # string
        print('-' * 50)
        print(my_file.readable()) # check for status - opened for read
        print(my_file.writable()) # check for status - opened for write
        print(my_file.name)       # Get file name
        print(my_file.encoding)   # Get encoding, ex. cp1252
        print(my_file.closed)     # Get status - closed or not
        my_file.truncate(8) # Truncate file up to 8 bytes



if __name__ == '__main__':
    main()