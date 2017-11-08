#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experimental crawler to grab data from websites. 
This project is for educational purposes only.

Usage:
    crawlyn BASEURLS... [--output=<OUTFILE>] [--proxyhost=<PROXYHOST> --proxyport=<PROXYPORT>] [--tor]
    crawlyn -h | --help
    crawlyn -t | --tor
    crawlyn -v | --version

Arguments:
    <OUTFILE>           Name output file.
    <PROXYHOST>         Specify the proxy host address.
    <PROXYPORT>         Specify the proxy port number.

Options:
    -h --help           Show this message.
    -t --tor            Run Crawlyn with Tor.
    -v --version        Show version.
"""

import logging
import sys

from . import crawlyn
from . import driver
from . import utils
from . import __version__
from docopt import docopt

def main():
    args = docopt(__doc__, version=__version__)

    proxy_host = args['--proxyhost']
    proxy_port = args['--proxyport']

    if sum(a is not None for a in (proxy_host, proxy_port)) == 1:
        logging.warning("Both proxy host address and port number needs to be set.")
        sys.exit(1)

    if proxy_port and not str(proxy_port).isdigit():
        logging.warning("Please input a valid proxy port number.")
        sys.exit(1)

    browser = driver.Browser(proxy_host, proxy_port, args['--tor'])
    crawler = crawlyn.Crawler(browser, args['BASEURLS'])
    results = utils.json_for(crawler.run(args))

    browser.quit()

    if args['--output'] is None:
        print(results)
    else:
        utils.save(results, args['--output'])

if __name__ == '__main__':
    main()
