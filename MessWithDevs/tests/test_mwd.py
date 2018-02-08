import unittest
import subprocess
import os

direc = os.path.dirname(os.path.realpath(__file__))

class Test_MWD(unittest.TestCase):
    def test_r_reverses_perfectly(self):
        subprocess.call(['cp', 'allRelevantChars.c', 'test.c'])
        subprocess.call(['python', '../mwd', direc + '/allRelevantChars.c'])
        subprocess.call(['python', '../mwd', direc + '/allRelevantChars.c', '-r'])

        with open('allRelevantChars.c', 'r') as converted:
            with open('test.c', 'r') as original:
                orig = original.readlines()
                conv = converted.readlines()
                self.assertEqual(len(orig), len(conv))
                self.assertEqual(orig, conv)
        subprocess.call(['rm', 'test.c'])



unittest.main()
