#!/usr/bin/env python3

# Python 3.9.5

# using_textwrap.py

# Purpose: Set the output width of the text in the console to a predetermined width.

# Dependency
import os
import textwrap

# First determine how many columns (white space characters) are available in the console.
os.get_terminal_size().columns

sample_text:str = """A quiet summer morning had risen up upon the great city. The clock in
the modern church steeple of the downtown district had not yet struck
seven, when the side door of one of the small buildings closed and a woman
came out into the silent street."""
  
print(textwrap.fill(sample_text, 65) # Set the output width to 65 columns
print(textwrap.fill(sample_text, 45) # Set the output width to 45 columns

print(textwrap.fill(sample_text, 65, initial_indent='    ')) # Begin the first line with an indentation.
print(textwrap.fill(sample_text, 65, subsequent_indent='    ')) # The first line not indented, but the following lines.
