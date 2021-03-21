# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/21 -*-

"""计数排序"""

import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)
    return li


if __name__ == '__main__':
    li = [random.randint(0, 100) for _ in range(1000)]
    print(f'排序前: {li}')
    print(f'排序后: {count_sort(li=li, max_count=100)}')
