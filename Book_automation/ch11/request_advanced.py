import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.twxt')

# this construction prints an error and  NOT stops if status of request != 200 OK
try:
    res.raise_for_status()
except Exception as exc:
    print('Error happened: %s' % (exc))

print(type(res))

# http return code
print(res.status_code)

# length of returned text
print(len(res.text))

# first 250 symbols of text
print(res.text[:250])