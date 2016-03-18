#! python2.7

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(name='unique',
      version='0.0.1',
      description='Unique Values ArcGIS tool helper',
      long_description=readme,
      author='Adam Marinelli',
      author_email='amarinelli@esri.ca',
      url='https://github.com/amarinelli/unique-value-domain',
      license=license,
      packages=find_packages(exclude=('tests'))
     )
