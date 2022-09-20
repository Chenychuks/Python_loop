#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-16
Purpose: Python Control flow Statements and Loops
"""


def string_slicing():
    name = input('Enter your name:')
    x = (name[0:2])
    print(x + '...' + x + '...' + name + '?')


string_slicing()
