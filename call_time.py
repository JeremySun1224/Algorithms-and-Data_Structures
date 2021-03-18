# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/12/27 -*-

import time


def call_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} running time is {t2 - t1}.')
        return result

    return wrapper
