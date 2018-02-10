#============================================================================
# Name        : setup.py
# Author      : Alex James Wright
# Version     : 0.1
# Copyright   : MIT
# Description : PyPi setup file
#============================================================================

from setuptools import setup

setup(name='MessWithDevs',
      version='0.1.2',
      description='Swaps characters in a text file with indistinguishable doppelgangers to break code (damage is reversible!)',
      url='https://github.com/AlexJamesWright/MessWithDevs',
      author='Alex James Wright',
      author_email='a.j.wright@soton.ac.uk',
      license='MIT',
      packages=['MessWithDevs'],
      entry_points={'console_scripts': ['mwd=MessWithDevs.commandLine:main']},
      include_package_data=True,
      keywords='MessWithDevs',
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
