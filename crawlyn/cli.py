#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experimental crawler to scrape internal links and email addresses 
from websites, including obfuscated email addresses. This project is 
for educational purposes only.

Usage:
    crawlyn [URLS ...] [--help] [--output=OUTFILE] [--version]

Options:
    -h --help                   Show this message.
    -o --output=OUTFILE         Name output file.
    -v --version                Show version.
"""

import json
import logging
import sys

from . import crawlyn
from . import __version__
from docopt import docopt

def json_for(results):
    """
    Serialize results to JSON.
    """
    return json.dumps(results, indent=4, sort_keys=True)

def save_results(results, output):
    """
    Save results to a file.
    """
    with open(output, 'w') as f:
        f.write(results + '\n')
        logging.warning("Wrote results to %s.", output)

def main():
    args = docopt(__doc__, version=__version__)

    if not args['URLS']:
        logging.warning("Please input at least one URL.")
        sys.exit(1)

    crawler = crawlyn.Crawler(args['URLS'])
    results = json_for(crawler.run(args))

    if args['--output'] is None:
        print(results)
    else:
        save_results(results, args['--output'])

if __name__ == '__main__':
    main()
