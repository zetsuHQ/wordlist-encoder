#!/usr/bin/python3

import hashlib
import base64



input_path = 'data/wordlist.txt'
wordlist = open(input_path, 'r')

hashed_path = 'data/hashed.txt'
hashed_writeable = open(hashed_path, 'w')   # As this file will be opened in both modes along the code,
hashed_readable = open(hashed_path, 'r')    # it's opening is already declared here in both ways.

encoded_path = 'data/encoded.txt'

num_lines = sum(1 for _ in open(input_path)) # Gets the number of lines in the input file



def string_to_hash():
    i = 1
    while i <= num_lines:
        next_line = wordlist.readline() 
        next_line = next_line[:-1] # Removes the newline (\n) character so it doesn't also gets hashed
        input_string = next_line  
        md5_hash = hashlib.md5(input_string.encode()).hexdigest() # Hashes the input string
        hashed_writeable.write(md5_hash+'\n')

        i += 1
    hashed_writeable.close()



def hash_to_base64():
    encoded = open(encoded_path, 'w')

    i = 1
    while i <= num_lines:
        next_line = hashed_readable.readline()
        next_line = next_line[:-1]  # Removes the newline (\n) character so it doesn't also gets converted to base64
        input_string = 'carlos:' + next_line   
        base64_string = base64.b64encode(bytes(input_string, 'utf-8')).decode('utf-8')
        encoded.write(f'{base64_string}\n')

        i += 1
    hashed_readable.close()
    encoded.close()



string_to_hash()
hash_to_base64()

wordlist.close()
