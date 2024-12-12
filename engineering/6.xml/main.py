from bs4 import BeautifulSoup
import requests


def main():
    html_doc = requests.get('https://httpbin.org').text
    #print(html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    print('*' * 50)
    print(soup.title.string)
    print('*' * 50)
    defs = soup.find("defs")
    print(defs)
    return



if __name__ == '__main__':
    main()