#!/usr/bin/env python3

# Python 3.9.5

# string_representation.py

# Purpose: Concept of string representation within a class.

class Car:
    def __init__(self, brand, size_class, name):
        self.brand = brand
        self.size_class = size_class
        self.name = name

    def __repr__(self):
        result = 'Brand: ' + self.brand + ', class: ' + self.size_class + ', name: ' + self.name
        return result

car1 = Car('Honda', 'Compact', 'Civic')
car2 = Car('BMW', 'Mid-size luxury', '5 Series')

print(car1)
print(car2)
