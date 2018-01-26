# -*- coding: utf-8 -*-
import sys

# Dictionary has the form    normal : pain in the arse version
diction = {';':';'}
# diction = {'r':'R'}

if sys.argv[1] == '-r':
    mode = 'r'
    revdiction = dict([[v, k] for k, v in diction.items()])
    useDict = revdiction
else:
    useDict = diction


with open("source.txt", 'r') as fin:
    with open("target.txt", 'w') as fout:
        for line in fin.readlines():
            string = ''
            for char in line:
                if char in useDict.keys() :
                    string += useDict[char]
                else:
                    string += char
            fout.write(string)
