# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Installation setup for unitexlemmatizer
"""

from setuptools import setup, find_packages

with open('README.rst', 'rb') as f:
    long_desc = f.read()

setup(name='unitexlemmatizer',
      version='1.0.0',
      description='A simple lemmatizer based on Unitex word lists',
      long_description=long_desc,
      author='Erick Fonseca',
      author_email='erickrfonseca@gmail.com',
      url='https://github.com/erickrf/unitex-lemmatizer',
      license='MIT',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
      ],
      keywords=['nlp', 'lemmatizer'],
      packages=find_packages()
      )
