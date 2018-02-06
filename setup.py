from setuptools import setup

setup(name='MessWithDevs',
      version='0.1',
      description='Swaps characters in a text file with indistinguishable partners to break code',
      url='https://github.com/AlexJamesWright/MessWithDevs',
      author='Alex James Wright',
      author_email='a.j.wright@soton.ac.uk',
      license='MIT',
      packages=['MessWithDevs'],
      scripts=['MessWithDevs/mwd'],
      include_package_data=True,
      install_requires=[
        'MessWithDevs'
      ],
      keywords='MessWithDevs',
      zip_safe=False)
