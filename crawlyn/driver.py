#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

_dir = os.path.dirname(os.path.abspath(__file__))

class Browser(webdriver.PhantomJS):
    def __init__(self, proxy_host=None, proxy_port=None, tor=False):
        self.proxy_host = '127.0.0.1' if tor else proxy_host
        self.proxy_port = '9050' if tor else proxy_port

        webdriver.PhantomJS.__init__(self,
                                     executable_path=self.phantomjs(),
                                     desired_capabilities=self.user_agent(),
                                     service_args=self.proxy(tor),
                                     service_log_path=os.path.devnull)

    def phantomjs(self):
        """
        Get path to PhantomJS executable.
        """
        arch = '64' if sys.maxsize > 2**32 else '32'
        path = '{0}/bin/phantomjs'.format(_dir)
        if 'darwin' in sys.platform:
            driver = r'{0}/macos/phantomjs'.format(path)
        elif 'linux' in sys.platform:
            driver = r'{0}/linux/{1}/phantomjs'.format(path, arch)
        elif 'win32' in sys.platform:
            driver = r'{0}/windows/phantomjs.exe'.format(path)
        return driver

    def proxy(self, tor):
        """
        Set proxy.
        """
        if tor or all((self.proxy_host, self.proxy_port)):
            return [
                '--proxy={0}:{1}'.format(self.proxy_host, self.proxy_port),
                '--proxy-type={0}'.format('socks5' if tor else 'http'),
            ]
        return

    def user_agent(self):
        """
        Change user agent.
        """
        dc = DesiredCapabilities.PHANTOMJS.copy()
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) " \
                     "AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/55.0.2883.95 Safari/537.36s"
        dc['phantomjs.page.customHeaders.User-Agent'] = user_agent
        return dc
