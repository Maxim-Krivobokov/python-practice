import os 

for foldername, subfolders, filenames in os.walk('testfolder_main'):
    print('current folder - ' + foldername)

    for subfolder in subfolders:
        print('subfolder of '+ foldername + ': ' + subfolder)

    for filename in filenames:
        print('file in folder ' + foldername + ': ' + filename)

    print('')

    