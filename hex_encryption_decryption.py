#!/usr/bin/env python3

# Python 3.9.5

# hex_encryption_decryption.py

sample:str = 'Sample_Text_123!='

encoded_sample = sample.encode("utf-8").hex()
print(encoded_sample)

decoded_sample = bytes.fromhex(encoded_sample).decode("utf-8")
print(decoded_sample)

sample == decoded_sample
