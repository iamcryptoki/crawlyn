#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def scrape(out, key, regex, html, host):
    pattern = re.compile(regex, re.MULTILINE | re.IGNORECASE)
    data = re.findall(pattern, html)
    for d in data:
        if not key in out[host].keys():
            out[host][key] = []
        if d not in out[host][key]:
            out[host][key].append(d)

def email_addresses(out, host, html):
    """
    Extract email addresses.
    """
    regex = r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b"
    scrape(out, 'emails', regex, html, host)

def phone_numbers(out, host, html):
    """
    Extract phone numbers.
    """
    regex = (r"(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}"
             r"|\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b")

    scrape(out, 'phone_numbers', regex, html, host)
