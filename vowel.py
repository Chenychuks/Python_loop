#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-09-16
Purpose: Python Control flow Statements and Loops
"""

name = input('Enter your name: ').lower()
vowel = ['a', 'e', 'i', 'o', 'u']
found_vowel = []

for item in name:
    if item in vowel:
        #print(item, end='')
        print(found_vowel.append(item))
print(found_vowel)
