#!/usr/bin/env python3

# usage:
# *.py input_file_name.extension output_file_name.extension

# Author: Suzie Hoops
#   Purpose: Find all (single-word) palindromes in an input file, print
#   frequency of occurrences to an output file.

import sys
import string
import re
import os

# Get file names (read in as strings from command line)
infile = sys.argv[1]
outfile = sys.argv[2]

# Define function for checking palindrome status
def palindrome(word):
    # compare 'word' to reverse, using string[begin:end:step] syntax
    # return boolean value: true = palindrome, false = not
    return word == word[::-1]

# Prepare a dictionary called 'pds' for palindromes
pds = {}

# Define function for updating dictionary
def updateDict(word, pds):
    # check for word in dictionary
    if word not in pds:
        pds[word] = 1
        return pds
    else:
        pds[word] += 1
        return pds

# Read in input file
print('Reading file ' + infile + '...\n')
with open(infile, "r") as f1:
    # read line by line
    for line in f1:
        # split line by white spaces to get words
        for word in line.split():
            # strip word of punctuation, make word entirely lowercase
            word = re.sub(r'[^\w]', '', word.lower())
            # check palindrome status
            if palindrome(word) and len(word) > 1:
                pds = updateDict(word, pds)
            else:
                continue
    # close file when outer loop closes
    f1.close()

# Print to output file
print('Printing to ' + outfile + '...\n')
with open(outfile, "w") as f2:
    # dictionary 'pds' contains all info, cycle through list of items
    for item, val in pds.items():
        f2.write(" ".join((item, str(val), '\n')))
    f2.close()

print('Done!')