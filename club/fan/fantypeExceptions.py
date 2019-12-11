# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:32:33 2019

@author: dhata
"""

class ViewsException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value+' is an invalid method to View matches'))
    
class TicketException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        if self.value == "Yes" or self.value == "yes" or self.value == "no" or self.value == "No" or self.value == "NO" or self.value == "YES":
            return(repr('Enter True or False! Not:'+str(self.value)))
       