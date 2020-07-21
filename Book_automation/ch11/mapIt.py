#! python3
# mapiT.py - запускает карту в браузере, извлекая почтовый адрес из командной строки или буфера обмена. 

#vtest address New-Zealand Oakland Queen street

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # getting mail address from arguments
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print(address)

webbrowser.open('https://www.google.com/maps/place/' + address)
