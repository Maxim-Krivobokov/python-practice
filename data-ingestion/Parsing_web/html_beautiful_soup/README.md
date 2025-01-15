# Parsing HTML
We should remember, that parsing HTML is much more complicated than making requests to the API

beautifulsoup - is the most common lib for html parsing
bs4 - beautifulsoup

fx.html - page for foreign exchange rates

b.soup has several parsers. For html for example
After parsing, we can iterate on 'tr' and 'td' elements

# Describing BeautifulSoup
short name BS for convenience
installation:
``` pip install beautifulsoup4 ```

Basic usage:

1. import and create a soup object 
    - load HTML or XML contenbt into BS object for parsing
2. Navigate and search
    - use methods and attribiutes to navigate the parse tree and extract data
3. Manipulate
    - Modify the HTML or XML content if needed.

Parsing HTML example:
```
from bs4 import BeautifulSoup

# Example HTML
html_doc = """
<html>
    <head><title>Example Page</title></head>
    <body>
        <h1>Main Heading</h1>
        <p class="intro">This is a paragraph.</p>
        <a href="http://example.com">Example Link</a>
    </body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# Extract the title
title = soup.title.string
print("Title:", title)

# Find the first paragraph
first_paragraph = soup.find('p')
print("First Paragraph:", first_paragraph.text)

# Extract the link
link = soup.find('a')['href']
print("Link:", link)

```