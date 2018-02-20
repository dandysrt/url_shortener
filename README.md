# url_shortener
pythonic URL shortening service  Dandy Martin

## Description
URLSHORTENER is an importable library that generates shortened references to
longer URLS.
* URL storage service is customizable depending on preference with adherence
to the URLTABSTRACT abstract class' function calls.
* In order to use a custom storage service, build your own urltable.py with URLTABLE
class object, and wrap your storage and retrieval calls according to the URLTABSTRACT
function calls.
* Updated to utilize an ascii-based bijective function to randomly generate hash keys
whose characters fall in the range a-zA-Z0-9, and appending their integer values together
instead of simply summing them - Vastly increasing the range of keys available, and minimizing
risk of collision.
* Additionally allows custom hash key range (variable from 1-N)
* By default, an explicit, dynamic hash-table implementation is already provided...
(I realize Python already has a dictionary that can be used instead, this was more fun).
Simply follow the Quick Start Guide to get started.

## Features
* Importable Class-based structure
* Abstract class for 'API' guidance

## Quick Start Guide
1. Import the shorten.py URLSHORTENER class
```python
    from shorten import URLSHORTENER
```
2. Initialize URLSHORTENER with your host, table size, and url-object time-to-live values
```python
    myshortener = URLSHORTENER('www.myhost[.]com', 999, 3)
```
3. Generate a shortened URL with a call to get_short_url function, passing the long_url. If your host is http unsecured, set the second optional value to True
```python
    long_url = 'www.somehost[.]net/there/is/a/whole/bunch/of?what'
    short_url = myshortener.get_short_url(long_url) # if secured
    us_short_url = myshortener.get_short_url(long_url, http=True)  # if unsecured

    >>> print short_url
    'https://www.myhost[.]com/jt104'
    >>> print us_short_url
    'http://www.myhost[.]com/jt104'
```
4. Similarly, in order to retrieve the long-version of your url, simply call get_long_url with the shortened url value
```python
    long_url = myshortener.get_long_url(short_url)

    >>> print long_url
    'www.somehost[.]net/there/is/a/whole/bunch/of?what'
```

### Requirements
build requires python stdlib imports: struct, random, and datetime
#### Special requirements are a custom urltable.py classfile with a URLTABLE class object though a default has been provided
