# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/22 -*-

"""基数排序"""

import random


def radix_sort(li):
    max_num = max(li)
    it = 0  # 迭代次数
    while 10 ** it <= max_num:
        # 分桶
        buckets = [[] for _ in range(10)]  # 创建桶
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 把数重新写回li
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1
    return li


if __name__ == '__main__':
    li = list(range(100))
    random.shuffle(li)
    print(f'排序前: {li}')
    print(f'排序后: {radix_sort(li=li)}')
