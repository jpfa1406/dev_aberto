#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_joaopfa2',
      version='0.1',
      packages=['dev_aberto'],
      scripts=['scripts/hello.py'],
      install_requires=[
        'requests',
        'setuptools'
      ]
      )
