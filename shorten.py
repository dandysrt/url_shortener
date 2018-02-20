#!/usr/bin/python

import random
import struct
from urltable import URLTABLE


class URLSHORTENER(object):
    '''
     @ClassDesc: Class for shortening long URLs
    '''

    def __init__(self, host, size, max_keysize=7, delta=1):
        '''
         @Desc: class constructor
         @Params: host - hostname for shortened URL,
          size - size of URLTABLE object,
          max_keysize - maximum number of characters to append to shortened url,
          delta - time in hours for URLOBJECT Time To Live(TTL)
        '''
        self.host = str(host)  # explicitly ensure host is string value
        self.urltable = URLTABLE(size, delta)
        self.max = max_keysize

    def build_key(self, seed=None):
        '''
         @Desc: function to build URLTABLE key
         @Params: seed - optional seed value
         @Return: i_key - integer representation of key,
           s_key - string representation of key
        '''
        i_key = ''
        random.seed(seed)
        size = random.randint(1, self.max)  # magic number, but we've got to limit it somewhere
        klist = ['>{0}B'.format(size)]
        for _ in range(size):
            asc = 0
            base = random.randint(48, 57)   # ascii values for 0-9
            mult = random.randint(1, 2)     # ascii a-z is nearly double 0-9 values
            add = 0
            if mult > 1:
                add = random.randint(1, 8)  # lower to upper range of values for a-z
                if random.randint(0, 1):
                    add-= 32                # randomly decide to uppercase
            asc = (base * mult) + add
            klist.append(asc)
            i_key+= str(asc)
        s_key = struct.pack(*klist)
        return int(i_key), s_key

    def build_url(self, host, string_key, http=False):
        '''
         @Desc: function to build shortened url
         @Params: host - short url hostname,
           string_key - generated string key,
           http - host is http unsecured(True/False)
         @Return: shortened url
        '''
        header = 'https://{0}'.format(host)
        if http:
            header = 'http://{0}'.format(host)
        if 'http' in str(host):  # ensure host value is string
            header = str(host)
        return '/'.join([header, string_key])

    def push_to_table(self, int_key, string_key, long_url):
        '''
         @Desc: function to push long_url to URLTABLE object
         @Params: int_key - generated integer key,
           string_key - generated string key,
           long_url - long url
         @Return: URLTABLE push function return value
        '''
        return self.urltable.push(int_key, string_key, long_url)

    def get_long_url(self, short_url):
        '''
         @Desc: function to retrieve long_url from URLTABLE object
         @Params: short_url - shortened url
         @Return: long url
        '''
        return self.urltable.retrieve(short_url.split('/')[-1])  # split and grab key from end of url

    def get_short_url(self, long_url, http=False):
        '''
         @Desc: function to generate shortened url, and
           push generated URLOBJECT to URLTABLE object
         @Params: long_url - long url, http - host is unsecured(True/False)
         @Return: shortened url
        '''
        i_key, s_key = self.build_key(long_url)
        self.push_to_table(i_key, s_key, long_url)
        return self.build_url(self.host, s_key, http)
