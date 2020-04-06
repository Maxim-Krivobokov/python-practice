#! python3
# adding markers from Wikipedia to the begginning of every line of text, saved to the bufer

import pyperclip

text = pyperclip.paste()

# TODO: split strings and add *
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    print(lines[i])

text = '\n'.join(lines)
pyperclip.copy(text)
