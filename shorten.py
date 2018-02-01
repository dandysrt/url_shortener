#!/usr/bin/python

import os, sys
import random
import struct
from urltable import URLTABLE


class URLSHORTENER(object):
    '''
     @Desc:
    '''

    def __init__(self, host, size, delta=1):
        self.host = host
        self.urltable = URLTABLE(size, delta)


    def build_key(self, seed=None):
        klist = ['>5B']
        i_key = 0
        random.seed(seed)
        for _ in range(5):
            asc = 0
            base = random.randint(48, 57)   # ascii values for 0-9
            mult = random.randint(1, 2)     # ascii a-z is nearly double 0-9 values
            add = 0
            if mult > 1:
                add = random.randint(1, 8)
            asc = (base * mult) + add
            klist.append(asc)
            i_key+= asc
        s_key = struct.pack(*klist)
        return i_key, s_key

    def build_url(self, host, string_key, http=False):

        header = 'https://{0}'.format(host)
        if http:
            header = 'http://{0}'.format(host)
        if 'http' in host:
            header = host
        return '/'.join([header, string_key])


    def push_to_table(self, int_key, string_key, long_url):
        self.urltable.push(int_key, string_key, long_url)

    def get_long_url(self, short_url):
        return self.urltable.retrieve(short_url.split('/')[-1]) # split and grab key from end of url

    def get_short_url(self, long_url, http=False):
        i_key, s_key = self.build_key(long_url)
        self.push_to_table(i_key, s_key, long_url)
        return self.build_url(self.host, s_key, http)
