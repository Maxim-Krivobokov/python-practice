import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# this function causes an error and stop if status of request != 200 OK
res.raise_for_status()


print(type(res))

# http return code
print(res.status_code)

# length of returned text
print(len(res.text))

# first 250 symbols of text
print(res.text[:250])