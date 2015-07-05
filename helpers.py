#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python source code - replace this with a description of the code
and write the code below this text.
"""

from bs4 import BeautifulSoup
from subprocess import check_output

import re
import requests

aspects = {"1.8": "16x9",
           "1.6": "16x10"}


def scrapeSite(url):
    raw = requests.get(url)
    page = BeautifulSoup(raw.text)
    return page


def getRes():
    # Get screen info from xrandr
    xrandrRaw = check_output("xrandr")
    xrandr = xrandrRaw.decode("utf-8")

    # Find resolution
    p = re.search("\s+(\d+)x(\d+).*\*", xrandr)
    return p.group(1, 2)


def getRatio():
    res = getRes()
    width = int(res[0])
    height = int(res[1])

    # ratio = width / height
    ratio = format((width / height), '.1f')
    aspect = aspects[ratio]
    return aspect
