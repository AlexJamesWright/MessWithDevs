#============================================================================
# Name        : test_mwd.py
# Author      : Alex James Wright
# Version     : 0.1
# Copyright   : MIT
# Description : Tests for command line tool, ensures process reverses
#============================================================================

import unittest
import subprocess
import os

direc = os.path.dirname(os.path.realpath(__file__))

class Test_MWD(unittest.TestCase):
    def test_r_reverses_perfectly(self):
        subprocess.call(['cp', 'allRelevantChars.c', 'test.c'])
        subprocess.call(['python', '../__init__.py', direc + '/allRelevantChars.c'])
        subprocess.call(['python', '../__init__.py', direc + '/allRelevantChars.c', '-r'])

        with open('allRelevantChars.c', 'r') as converted:
            with open('test.c', 'r') as original:
                orig = original.readlines()
                conv = converted.readlines()
                self.assertEqual(len(orig), len(conv))
                for charOrig, charConv in zip(orig, conv):
                    self.assertEqual(charOrig, charConv)
        subprocess.call(['rm', 'test.c'])



unittest.main()
