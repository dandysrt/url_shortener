#!/usr/bin/python
import os, sys
from urltable_abstract import URLTABSTRACT, URLOBJECT
from datetime import datetime, timedelta
import struct

class URLTABLE(URLTABSTRACT):
    '''
     @ClassDesc: dynamic hash-table class inherits URLTABSTRACT to adhere to API
    '''

    def __init__(self, size, delta=1):
        '''
         @Desc: URLTABLE constructor
         @Params: size - maximum hash-list size, delta - number in hours
           for Time To Live (TTL) of URLOBJECTS
        '''
        super(URLTABLE, self).__init__()
        self.hashlist = [list() for _ in range(size)] # initialize hashtable to set size
        self.seed = size                # seed is the size of hashlist "Y" dimension
        self.delta = timedelta(hours=delta) # TTL for URLOBJECTS

    def push(self, int_key, string_key, long_url):
        '''
         @Desc: function to add to hash-list
         @Params: int_key - generated integer key,
           string_key - generated string key,
           long_url - full url
         @Return: True - if item successfully placed in list,
            False - if item not successfully placed
         @AdditionalInfo: O(1)
        '''
        key = int_key % self.seed
        try:
            self.hashlist[key].append(URLOBJECT(key, string_key, long_url, datetime.utcnow()))
            return True
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
        key = int_key % self.seed
        try:
            for i in range(len(self.hashlist[key])):
                try:
                    u_obj = self.hashlist[key][i]
                except IndexError:
                    return None
                if not datetime.utcnow() - u_obj.time > self.delta:
                    if u_obj.str_key in string_key: # if our time and key is valid, return the url
                        return u_obj.url
                else:
                    self.hashlist[key].pop(i) # rid ourselves of objects that are expired
            return None # if we did not encounter our key, return nothing
        except Exception as e:
            raise e
