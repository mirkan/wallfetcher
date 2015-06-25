#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Automatically fetch wallpapers and enable them in a
desktop environment.
"""

from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from subprocess import check_output
import re
import os
import requests

out_folder = "img/"

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


def reddit():
    url = 'http://reddpics.com/r/wallpapers/'

    reddit_page = requests.get(url)

    page = BeautifulSoup(reddit_page.text)

    for link in page.findAll('li', 'new', limit=3):
        validUrl = re.compile("^https?://.*.(jpg|png)$")
        if validUrl.match(link["page"]):
            print ("Link: %s" % link["page"])
            filename = link["page"].split("/")[-1]
            path = os.path.join(out_folder, filename)
            urlretrieve(link["page"], path)


def wallhaven():
    url = "http://alpha.wallhaven.cc/search?"\
        "q=%22nature%22&"\
        "categories=100&"\
        "purity=100&"\
        "ratios=" + getRatio() + "&"\
        "sorting=random&"\
        "order=desc&"
    page = scrapeSite(url)

    fullUrl = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
    for image in page.findAll('figure', limit=1):
        imageUrl = fullUrl + image["data-wallpaper-id"] + ".jpg"
        print ("Image: %s" % imageUrl)
        filename = image["data-wallpaper-id"] + ".jpg"
        path = os.path.join(out_folder, filename)
        urlretrieve(imageUrl, path)

    # Convert to current resolution if necessary
    screenres = getRes()
    fileres =

wallhaven()
