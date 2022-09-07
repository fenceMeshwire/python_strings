#!/usr/bin/env python3

# Python 3.9.5

# xx_using_string_module.py

# Dependency
import string

drink = 'Ice Tea'
flavor = 'good'
calories = 1000

output = string.Template('$drink has a $flavor taste and a gross calorific value of $calories kcal.')
output.substitute(vars())
