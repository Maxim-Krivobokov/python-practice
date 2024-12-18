# Selenium
That is a framework to automate work with a browser (for example, run javascript)

```from selenium import webdriver```
1) start web-server httpd.py (8985)

2) Install Selenium driver for your browser.

3) How does work fx.py:
   - from Selenium we import driver for our browser (Firefox)
   - run driver.get('localhost:8985') to load the webpage with JS code
   - use method find_elements_by_tag_name() to find '.date' selector
     - for every found element, we extract the text, print it, etc.