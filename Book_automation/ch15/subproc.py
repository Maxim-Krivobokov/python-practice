import subprocess
import platform
import sys
import os

print('sys plaform :')
print(sys.platform)

print('os name :')
print(os.name)

print('platform.plaform :')
print(platform.platform())
if (sys.platform == 'win32'):
    print('Starting windows calc')
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
else:
    print('linux calc')
    subprocess.Popen('/usr/bin/gnome-calculator')