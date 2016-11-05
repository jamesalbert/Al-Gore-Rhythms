#!/usr/bin/env python

from setuptools import setup

setup(name='Al-Gore-Rhythms',
      version='0.1',
      description=('graphing/sorting Al Gore Rhythms with data structures'),
      author='James Albert, Hector Flores',
      author_email='jalbert1@uci.edu, hflores@uci.edu',
      url='https://github.com/jamesalbert/Al-Gore-Rhythms',
      packages=['algore',
                'algore.graphing',
                'algore.sorting',
                'algore.finding',
                'algore.structures'],
      install_requires=['cycler',
                        'decorator',
                        'matplotlib',
                        'networkx',
                        'numpy',
                        'pyparsing',
                        'six'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest',
                     'pytest-cov',
                     'pytest-pep8',
                     'pytest-flakes',
                     'pyflakes'])
