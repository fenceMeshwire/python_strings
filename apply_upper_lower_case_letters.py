#!/usr/bin/env python3

# Python 3.9.5

# apply_upper_lower_case_letters.py

# Sequence of the individual steps:
text = 'STATION 5: ERROR ON LABEL ASSIGNMENT - CODE: 290'

# 1. Convert all string characters to lower case characters
text = text.lower()

# 2. Split all characters of the string at the white space character.
text = text.split()

# 3. Set rules for the upper and lower case characters and append the characters to a list. 
text = [word.capitalize() if len(word) > 4 else word.lower() for word in text]

# 4. Concatenate the list elements to a single string, separated by a white space character for each word.
text = ' '.join(text)

# 5. Print result
print(text)


# Representation of the individual steps in a function:
def transform_letters(text):
    text = text.lower()
    text = text.split()
    text = [word.capitalize() if len(word) > 4 else word.lower() for word in text]
    text = ' '.join(text)
    return text

if __name__ == '__main__':
    text = 'STATION 5: ERROR ON LABEL ASSIGNMENT - CODE: 290'
    result = transform_letters(text)
    print(result)
