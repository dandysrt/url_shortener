# url_shortener
pythonic URL shortening service

## Features
* Importable Class-based structure
* Abstract class for 'API' guidance

## Quick Usage Guide
1. Import the shorten.py URLSHORTENER class
```python
    from shorten import URLSHORTENER
```
2. Initialize URLSHORTENER with your host, table size, and url-object time-to-live values
```python
    myshortener = URLSHORTENER('www.myhost.com', 999, 3)
```
3. Generate a shortened URL with a call to get_short_url function, passing the long_url. If your host is http unsecured, set the second optional value to True
```python
    short_url = myshortener.get_short_url('www.somehost.net/there/is/a/whole/bunch/of?what') # if secured
    us_short_url = myshortener.get_short_url('www.somehost.net/there/is/a/whole/bunch/of?what', http=True)  # if unsecured
```
4. Similarly, in order to retrieve the long-version of your url, simply call get_long_url with the shortened url value
```python
    long_url = myshortener.get_long_url(short_url)
```

### Requirements
build requires python stdlib imports: struct, random, and datetime
#### Special requirements are a custom urltable classfile with a URLTABLE class object though a default has been provided
