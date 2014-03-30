import os
from glob import glob
from setuptools import setup, find_packages

# Setup flags and parameters
pkg_name = 'libbot'  # top-level package name

# Cache readme contents for use as long_description
readme = open('README.md').read()

# Call setup()
setup(
  name=pkg_name,
  version='0.1',
  description='Library of common bot functions',
  long_description=readme,
  url='https://github.com/IEEERobotics/libbot',
  author='IEEE Robotics Team',
  author_email='group-ieee-robotics@ncsu.edu',
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
  install_requires=[
    'PyYAML'
  ],
  test_suite=(pkg_name + '.tests'),
  platforms='any',
  keywords='lib library bot ieee logger config',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.7',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ])
