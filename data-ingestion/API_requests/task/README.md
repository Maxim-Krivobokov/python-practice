# Find most common countries

I have a gzip compressed server log in the following format:
```
    133.43.96.45 - - [01/Aug/1995:00:00:22 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
    205.163.36.61 - - [01/Aug/1995:00:02:01 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
```

DOD:
return the 'n' most common countries in the log.

To convert an IP to a country, need to call the GeoIP server that runs on the localhost port 8988 (geoip.py).

Example HTTP request:
```GET /geoip=123.123.12.23```

Response in JSON:
```{'ip': "205.163.36.61", "iso": "US"}```

In case of unknown IP, server will return HTTP 404.
For authentication, should use bearer token 'l3tm3in'


# Useful libs that were used:
collections - Counter

functools - lru_cache
@lru_cache - decorator
ipaddress -  IPv4Address

