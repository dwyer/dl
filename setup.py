#-*-coding:utf-8-*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup

setup(
    name='dl',
    version='0.1',
    description='A command-line downloader.',
    author='Casey Dwyer',
    author_email='caseydwyer@gmail.com',
    url='https://github.com/dwyer/dl',
    license='BSD',
    scripts=['dl'],
    install_requires=[
        'beautifulsoup4',
    ],
)
