#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlretrieve
import re
import os
import helpers


def reddit():
    # Get URL
    url = 'http://reddpics.com/r/wallpapers/'
    page = helpers.scrapeSite(url)

    for link in page.findAll('li', 'new', limit=3):
        validUrl = re.compile("^https?://.*.(jpg|png)$")
        if validUrl.match(link["page"]):
            print ("Link: %s" % link["page"])
            filename = link["page"].split("/")[-1]
            path = os.path.join(out_folder, filename)
            urlretrieve(link["page"], path)


def wallhaven(out_folder):
    # Get resolution, e.g '1920x1080'
    res_list = helpers.getRes()
    res = res_list[0] + "x" + res_list[1]

    # Scrape site
    url = "http://alpha.wallhaven.cc/search?"\
        "q=%22nature%22&"\
        "categories=100&"\
        "purity=100&"\
        "resolutions=" + res + "&"\
        "sorting=random&"\
        "order=desc&"
    page = helpers.scrapeSite(url)

    # Download jpgs
    fullUrl = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
    for image in page.findAll('figure', limit=1):
        imageUrl = fullUrl + image["data-wallpaper-id"] + ".jpg"
        print ("Image: %s" % imageUrl)
        filename = res + "_" + image["data-wallpaper-id"] + ".jpg"
        path = os.path.join(out_folder, filename)
        urlretrieve(imageUrl, path)
