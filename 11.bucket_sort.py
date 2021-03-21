# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/21 -*-

"""桶排序"""


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for val in li:
        i = min(val // (max_num // n), n - 1)  # i表示val放到几号桶里
        buckets[i].append(val)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break 