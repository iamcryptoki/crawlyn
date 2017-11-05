#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import crawlyn

from setuptools import setup

setup(
    name='crawlyn',
    version=crawlyn.__version__,
    description="Experimental crawler to grab data from websites.",
    long_description=open('README.txt').read(),
    author='Galou Gentil',
    author_email='hello@cryptoki.fr',
    url='https://github.com/iamcryptoki/crawlyn',
    license='MIT',
    keywords='crawler, email, links, security, website',
    packages=['crawlyn'],
    package_data={
        'crawlyn' : [
            'bin/phantomjs/linux/32/phantomjs',
            'bin/phantomjs/linux/64/phantomjs',
            'bin/phantomjs/macos/phantomjs',
            'bin/phantomjs/windows/phantomjs.exe'
        ]
    },
    install_requires=['docopt', 'lxml', 'selenium'],
    entry_points={
        'console_scripts': [
            'crawlyn=crawlyn.cli:main',
        ]
    }
)
