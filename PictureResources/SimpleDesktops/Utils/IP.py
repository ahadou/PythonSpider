# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     IP
   Description :
   Author :       Giyn
   date：          2020/9/5 22:22:01
-------------------------------------------------
   Change Activity:
                   2020/9/5 22:22:01
-------------------------------------------------
"""
__author__ = 'Giyn'

import requests
import re
import random


def get_ip():
    """

    Get proxy IP

    Args:
        None

    Returns:
        proxies: proxy IP list

    """
    proxies = []  # storage agent IP

    url = 'http://127.0.0.1:5000/get_all/'
    res = requests.get(url=url)

    ip = re.findall(r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]):\d{2,6}',
                    res.text)  # extract IP

    # save to proxies list
    for i in range(10):
        one_ip = random.choice(ip)
        proxies.append({'https': 'https://' + one_ip, 'http': 'http://' + one_ip})
    return proxies
