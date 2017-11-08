#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import re

from bs4 import BeautifulSoup
from collections import deque
from selenium import webdriver
from urllib.parse import urldefrag, urljoin, urlparse

_dir = os.path.dirname(os.path.abspath(__file__))

class Crawler(object):
    def __init__(self, browser, base_urls):
        self.base_urls = base_urls
        self.browser = browser
        self.crawled_urls = []
        self.results = {}
        self.url_queue = {}

    def get_page_source(self, url):
        """
        Get the HTML source for the given URL.
        """
        try:
            self.browser.get(url)
            return self.browser.page_source
        except Exception as e:
            logging.exception(e)

    def get_page_links(self, base, soup):
        """
        Get all internal links for the given URL.
        """
        for link in soup.find_all('a', href=True):
            link = link['href']
            url = urljoin(base, urldefrag(link)[0])
            if url not in self.url_queue and url not in self.crawled_urls:
                if url.startswith(base):
                    self.url_queue.append(url)

    def get_page_emails(self, host, html):
        """
        Extract all email addresses from the given HTML.
        """
        pattern = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b',
                             re.MULTILINE | re.IGNORECASE)
        emails = re.findall(pattern, html)
        for email in emails:
            if not 'emails' in self.results[host].keys():
                self.results[host]['emails'] = []
            if email not in self.results[host]['emails']:
                self.results[host]['emails'].append(email)

    def get_soup(self, html):
        if html is not None:
            return BeautifulSoup(html, 'lxml')
        else:
            return

    def run(self, args):
        for base in self.base_urls:
            host = urlparse(base).hostname
            self.url_queue = deque([base])
            while len(self.url_queue):
                current_url = self.url_queue.popleft()
                self.crawled_urls.append(current_url)

                if not host in self.results.keys():
                    self.results[host] = {}
                if not 'urls' in self.results[host].keys():
                    self.results[host]['urls'] = []
                self.results[host]['urls'].append(current_url)

                scripts = re.compile(r'<(script).*?</\1>(?s)')
                html = scripts.sub('', self.get_page_source(current_url))

                self.get_page_emails(host, html)

                soup = self.get_soup(html)
                if soup is not None:
                    self.get_page_links(base, soup)

        return self.results
