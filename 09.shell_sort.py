# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/21 -*-

"""希尔排序"""

import random


def insert_sort_gap(li, gap):
    """
    分组insert sort
    :param li:
    :param gap: 分的组
    :return:
    """
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp
    return li


def shell_sort(li):
    """希尔排序"""
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li=li, gap=d)
        d //= 2
    return li


if __name__ == '__main__':
    li = list(range(100))
    random.shuffle(li)
    print(f'排序前: {li}')
    shell_sort(li=li)
    print(f'排序后: {li}')
