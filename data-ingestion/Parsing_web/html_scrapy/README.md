# Scrapy framework
It is an open-source framework


# Steps to reproduce exercise:
1) start httpd.py local web server
  - it will work on port 8987

2) install scrapy
https://docs.scrapy.org/en/latest/intro/install.html
https://docs.scrapy.org/en/latest/intro/overview.html

3) create scrapy project
```scrapy startproject fx```

4) start crawler:
```cd fx; scrapy crawl fx -o fx.jl```
5) result will be stored in fx.jl in json format
