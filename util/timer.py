#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convenience deocrator to time and print function execution timer

adapted from
"""

import functools
import itertools
import util
import logging

import datetime as dt
import functools as ft
from time import time

# _log = logging.getLogger(level="INFO")


def timer(f):
    @ft.wraps(f)
    def wrap(*args, **kw):
        start = time()
        # _log.info(f"function {f.__name__} started")
        print(f"function {f.__name__} started {dt.datetime.now().strftime('%H:%M:%S')}")
        result = f(*args, **kw)
        end = time()
        print(f'func:{f.__name__} took: {end-start:.4f} seconds')  # args:[{args}, {kw}]
        return result
    return wrap
