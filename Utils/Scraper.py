"""
-------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 18:14:58
# @Author  : Giyn
# @Email   : giyn.jy@gmail.com
# @File    : Scraper.py
# @Software: PyCharm
-------------------------------------
"""

import requests
import logging
import time
import os
from lxml import etree
from faker import Faker

faker = Faker()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')  # log information settings


class Scraper:
    def __init__(self, name, URL):
        self.name = name
        self.URL = URL

    def get_html(self, url):
        """

        Get page

        Args:
            url: URL

        Returns:
            res: response

        """
        while True:
            try:
                time.sleep(1)
                res = requests.get(url, headers={'User-Agent': faker.user_agent()})
                if res.status_code == 200:
                    return res
            except Exception as e:
                logging.ERROR(e)

    def parse_html(self, html, xpath_exp):
        """

        Parse web pages and get sources

        Args:
            html: html
            xpath_exp: xpath expression

        Returns:
            sources: sources

        """
        doc = etree.HTML(html)
        xpath_expression = xpath_exp
        sources = doc.xpath(xpath_expression)

        logging.info("Successfully get sources!")

        return sources

    def download_img(self, url, dir_name):
        """

        Download image

        Args:
            url: image url

        Returns:
            None

        """
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        img = self.get_html(url).content  # return bytes type which is binary data
        img_name = ''

        with open('{}/{}.png'.format(dir_name, img_name), 'wb') as file:
            file.write(img)

        logging.info("Successfully download an image!")

    def __repr__(self):
        return '<Scraper: name = %s>' % self.name
