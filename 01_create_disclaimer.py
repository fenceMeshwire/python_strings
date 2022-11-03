#!/usr/bin/env python3

# Python 3.9.5

# 01_create_disclaimer.py

# Purpose: Create a two line disclaimer, e.g. for language separation in a document.

def create_disclaimer(txt, length, separator):
    top = separator * length
    side = int((length - len(txt)) / 2) * separator
    txt = " " + txt + " "
    disc = side + txt + side
    diff = len(disc) - len(top)
    if diff > 0:
        top = (length + diff) * separator
    return top, disc

if __name__ == '__main__':
    txt = 'English Version'
    length = 70
    separator = '-'
    if len(length) > len(txt):
        top, disclaimer = create_disclaimer(txt, length, separator)
        print(top)
        print(disclaimer)
       
      
# Output:
# -----------------------------------------------------------------------
# --------------------------- English Version ---------------------------
