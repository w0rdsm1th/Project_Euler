#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convenience deocrator to time and print function execution timing

adapted from
"""

import functools
import itertools
import util

from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:%r args:[%r, %r] took: %2.4f sec' % \
              (f.__name__, args, kw, te-ts))
        return result
    return wrap
