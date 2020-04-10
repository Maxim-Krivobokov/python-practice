import traceback

try:
    raise Exception('This is an error message.')
except:
    errorFile = open('errlog.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Error info was written to errlog.txt')

    