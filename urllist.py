#!/usr/bin/python

import os, sys
from urltable_abstract import URLTABSTRACT, URLOBJECT
from datetime import datetime, timedelta




class URLLIST(URLTABSTRACT):
    '''
     @ClassDesc: hash-listing class inherits URLTABSTRACT to adhere to API
     @AdditionalClassInfo: more granular approach
    '''

    def __init__(self, size, delta=1):
        '''
         @Desc: URLTABLE constructor
         @Params: size - maximum hash-list size, delta - number in hours
           for Time To Live (TTL) of URLOBJECTS
        '''
        super(URLTABLE, self).__init__()
        self.hashlist = [None] * size   # initialize hashlist to set size
        self.seed = size                # seed is the size of hashlist
        self.delta = timedelta(hours=delta) # TTL for URLOBJECTS

    def push(self, int_key, string_key, long_url):
        '''
         @Desc: function to add to hash-list
         @Params: int_key - generated integer key,
           string_key - generated string key,
           long_url - full url
         @Return: True - if item successfully placed in list,
            False - if item not successfully placed,
            or entire list has been iterated
        @AdditionalInfo: O(1) best case, O(N) worst case
        '''
        key = self.seed % int_key
        try:
            if not self.hashlist[key]:
                self.hashlist[key] = URLOBJECT(key, string_key, long_url)
                return True
            else:
                while self.hashlist[key] and key < self.seed:
                    if datetime.utcnow() - self.hashlist[key].time > self.delta:
                        self.hashlist[key] = URLOBJECT(key, string_key, long_url)
                        return True
                    key+= 1
        except IndexError:
            return False
        except Exception as e:
            raise e


    def retrieve(self, string_key):
        '''
         @Desc: function to retrieve long url from hashlist
         @Params: string_key - generated string_key
         @Return: long url if successful, None if unsuccessful
         @AdditionalInfo: Best case O(1), worst case O(N)
        '''
        t = struct.unpack('>5B', string_key)
        int_key = t[0] + t[1] + t[2] + t[3] + t[4]
        key = self.seed % int_key
        while key < self.seed:
            u_obj = self.hashlist[key]
            if (datetime.utcnow() - u_obj.time) < self.delta \
              and u_obj.str_key in string_key and u_obj.int_key == key:
                return u_obj.url
            key+= 1
        else
            return None
