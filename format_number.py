#!/usr/bin/env python3

# Python 3.9.5

# xy_format_number.py

# Purpose: Formatting a number for a specific represenation, e.g. legends in matplotlib.pyplot

def format_number(value):
    swap_comma_dot = {ord('.'):',', ord(','):'.'}
    value = float(format(value, '0.2f'))
    value = format(value, ',').translate(swap_comma_dot)
    return value

if __name__ == '__main__':
    value = 2399.2314
    result = format_number(value)
    print(result, 'EUR') # 2.399,23 EUR
