# -*- coding: utf-8 -*-

import sys
from copy import deepcopy

# Dictionary has the form    normal : pain in the arse version
# semi colon is Greek question mark
# colon if Ethiopic wordspace
# period is Ethiopic tonal mark yizet
# single apostrophe is Canadian Syllabics West-Cree etc. etc. etc
opDictionary = {';':';', ':':'፡', '.':'᎐', "'":"ᑊ", '-':'‒', '"':'“', "'":'‛', \
                '|':'⎹', '/':'∕', ')':'⟯', '(':'⟮', '+':'⧾'}

# Objective is to get as many different errors as possible, so change available
# letters on an alternate basis
charDictionary = {'A':'Α', 'B':'Β', 'E':'Ε', 'Z':'Ζ', 'H':'Η', 'I':'Ι', 'K':'Κ', \
                  'M':'Μ', 'N':'Ν', 'O':'Ο', 'P':'Ρ', 'T':'Τ', 'Y':'Υ', 'X':'Χ', \
                  'F':'Ϝ', 'c':'ϲ', 'j':'ϳ', 'C':'Ϲ', 'S':'Ѕ', 'J':'Ј', 'e':'е', \
                  'o':'о', 's':'ѕ', 'i':'і', 'h':'һ', 'd':'ԁ', 'q':'ԛ', 'w':'ԝ'}

mode = sys.argv[1]
if mode == '-r':
    # Reverse mode, so swap keys and values
    useOpDict = dict([[v, k] for k, v in opDictionary.items()])
    useCharDict = dict([[v, k] for k, v in charDictionary.items()])
else:
    useOpDict = opDictionary
    useCharDict = charDictionary

# Keep track of which characters have been changed
charUsed = deepcopy(useCharDict)
for key in charUsed.keys():
    charUsed[key] = 0

# OK, start messing with their file
with open("source.txt", 'r') as fin:
    with open("target.txt", 'w') as fout:
        for line in fin.readlines():
            string = ''
            for char in line:
                if char in useOpDict.keys():
                    # Character is one of the operators
                    string += useOpDict[char]
                elif char in useCharDict.keys():
                    # Character is one of the chars to change
                    if mode == '-r':
                        # Always swap if in reverse mode
                        string += useCharDict[char]
                    elif charUsed[char]==1:
                        # Do not swap char this time
                        string += char
                        charUsed[char] = 0
                    elif charUsed[char]==0:
                        # Swap this time
                        string += useCharDict[char]
                        charUsed[char] = 1
                else:
                    # Character is not in dictionaries so do not change
                    string += char
            # Place this line in the target file
            fout.write(string)
# Fin.
