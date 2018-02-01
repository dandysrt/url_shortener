#!/usr/bin/python
from datetime import datetime

class URLOBJECT(object):
    '''
     @ClassDesc: URL attribute-holding object
    '''
    def __init__(self, int_key, str_key, url, time):
        '''
         @Desc: class constructor
         @Params: int_key - generated integer key,
           str_key - generated string key,
           url - long URL,
           time - datetime object
        '''
        self.int_key = int_key
        self.str_key = str_key
        self.url = url
        self.time = time

class URLTABSTRACT(object):
    '''
     @ClassDesc: Abstract class for inheritance
    '''
    def __init__(self, *args):
        pass

    def push(self, int_key, string_key, long_url):
        pass

    def retrive(self, string_key):
        pass
