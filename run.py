#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python source code - replace this with a description of the code
and write the code below this text.
"""

import sites
import os.path
import errno
from subprocess import call

# Path where images should be stored
path = os.environ['HOME'] + "/.local/wallfetch"
os.makedirs(path, exist_ok=True)

sites.wallhaven(path)
call(["feh", "--randomize", "--bg-fill", path])
