# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:05:34 2020

@author: Iari Severino
"""

def is_even():
    
    number = input("type a number: ")
    if int(number) % 2 == 0: 
        print('true')
    else: print('False')   

    
is_even()

#%%

def is_odd():
    
    number = input("type a number: ")
    if int(number) % 2 == 0: 
        print('False')
    else: print('True')   

    
is_odd()