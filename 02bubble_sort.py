# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/12/28 -*-

import random


def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:  # 要判断
            return li
    return li


li = [random.randint(0, 100) for i in range(10)]
# li = [5, 3, 6, 7, 9, 1, 8, 4]
print(li)
print(bubble_sort(li=li))
