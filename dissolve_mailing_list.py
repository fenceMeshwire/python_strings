#!/usr/bin/env python3

# Python 3.9.5

# dissolve_mailing_list.py

# Dependency
import os
from pathlib import Path

input_path = 'C:\\Users\\...\\'

os.chdir(input_path)
Path.cwd()

# Identities are formated from e.g. Microsoft Active Directory (AD):
# 'lastname firstname, department <firstname.lastname@domain.com>;
# The source is a single string, which is stored in a TXT file and
# originates from an email program (copy&paste from the address line).

with open ('emails.txt', 'rt', encoding='utf-8') as fin:
    txt = fin.read()

identities = txt.split(';')

with open('contacts.csv', 'wt', encoding='utf-8') as fout:
    fout.write('name' + ';' + 'department' + ';' + 'email-address' + '\n')
    for identity in identities:
        try:
            st1 = identity.split(',')
            st2 = st1[1].split('<')
            st1 = st1[0].strip(' ')
            st3 = [st1, st2[0].strip(' '), st2[1].strip('>')]
            fout.write(st3[0] + ';' + st3[1] + ';' + st3[2] + '\n')
        except IndexError:
            pass
