# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/21 -*-

"""桶排序"""

import random


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for val in li:
        i = min(val // (max_num // n), n - 1)  # i表示val放到几号桶里
        buckets[i].append(val)  # 把var加到桶里面
        for j in range(len(buckets[i]) - 1, 0, -1):  # 用类似插入排序的方法保持桶内顺序
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


if __name__ == '__main__':
    li = [random.randint(0, 10000) for _ in range(100000)]
    # print(f'排序前: {li}')
    print(f'排序后: {bucket_sort(li=li)}')
