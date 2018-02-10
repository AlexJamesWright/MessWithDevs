#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from copy import deepcopy

def ruin():
    if int(sys.version[0]) is not 3:
        print("Get a newer version of python, dammit!")
        sys.exit(-1)

    # Dictionary has the form    normal : pain in the arse version

    opDictionary = {';':';', ':':'፡', '.':'᎐', "'":"ᑊ", '-':'‒', '"':'“', "'":'‛', \
                    '|':'⎹', '/':'∕', ')':'⟯', '(':'⟮', '+':'⧾'}

    # Objective is to get as many different errors as possible, so change available
    # letters on an alternate basis to get undefined errors and whatever else it does
    # thats bad
    charDictionary = {'A':'Α', 'B':'Β', 'E':'Ε', 'Z':'Ζ', 'H':'Η', 'I':'Ι', 'K':'Κ', \
                      'M':'Μ', 'N':'Ν', 'O':'Ο', 'P':'Ρ', 'T':'Τ', 'Y':'Υ', 'X':'Χ', \
                      'F':'Ϝ', 'c':'ϲ', 'j':'ϳ', 'C':'Ϲ', 'S':'Ѕ', 'J':'Ј', 'e':'е', \
                      'o':'о', 's':'ѕ', 'i':'і', 'h':'һ', 'd':'ԁ', 'q':'ԛ', 'w':'ԝ'}

    EXE=[".cc", ".c", ".cpp", ".cxx", ".cu", ".c++", ".js", ".java", ".ii", \
    ".ixx", ".ipp", ".i++", ".inl", ".idl", ".ddl", ".odl", ".h", ".hh", ".hxx", ".hpp", ".h++", \
    ".cs", ".d", ".php", ".php4", ".php5", ".phtml", ".inc", ".m", ".md", ".mm", ".html", \
    ".dox", ".py", ".pyw", ".f90", ".f95", ".f03", ".f08", ".f", ".for", ".tcl", ".vhd", ".vhdl", \
    ".ucf", ".qsf"]

    inputFile=0
    FileList = []
    useExe = None
    userExeLen=1
    # Get files
    if '-e' in sys.argv:
        useExe = sys.argv[sys.argv.index('-e') + 1]
        userExeLen = len(useExe)
        EXE.append(useExe)
    # Get flags
    if '-r' in sys.argv:
        mode='-r'
    else:
        mode='-f'

    for i, arg in enumerate(sys.argv):
        if (arg.find('.')>=0 and not arg[-11:]=='__init__.py'):
            if (arg[-2:] in EXE or arg[-3:] in EXE or arg[-4:] in EXE or arg[-5:] in EXE or arg[-userExeLen:] in EXE) and arg!=useExe:
                inputFile+=1
                FileList.append(arg)

    if not inputFile:
        print("No valid input file.")
        sys.exit(-1)

    for File in FileList:
        subprocess.call(['cp', File, 'source.txt'])

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

        subprocess.call(['mv', 'target.txt', File])
        subprocess.call(['rm', os.getcwd() + '/source.txt'])
        # Fin.
if __name__=='__main__':
    ruin()
