#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-16
Purpose: Python Control flow Statements and Loops
"""

name = True
while name:
    my_name = input('Enter your name: ').upper().lower()
    if my_name == ('end').upper().lower():
        name = False
