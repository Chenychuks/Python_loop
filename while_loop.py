#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-16
Purpose: Python Control flow Statements and Loops
"""

name = input('Enter your name: ').upper().lower()
while name:
    if name == ('end').upper().lower():
        break
    else:
        print('my name is: ' + name)
