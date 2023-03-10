#!/usr/bin/env python3

# Python 3.9.5

# clear_filename_stem.py

# sample_further_text.xlsx
# |                  |   |
# stem               |   |
#                   dot  |    
#                       extension

def tidy_filename_stem(filename):
    for key in REPLACEMENT:
        value = REPLACEMENT[key]
        filename = filename.replace(key, value)
    filename = filename.split('_')
    filename = list(filter(None, filename))
    filename = '_'.join(filename)
    return filename

REPLACEMENT = {' ': '_', '&': 'and', '/': '_'}

if __name__ == '__main__':
    filename = 'some_ ugly / filename & stuff___'
    cleaned_filename = tidy_filename_stem(filename)
    print(cleaned_filename)
