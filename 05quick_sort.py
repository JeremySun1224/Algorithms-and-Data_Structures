# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/12/29 -*-

import random
import copy
from call_time import *


# 首先需要进行归位
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数，如果找到了，则把这个小的数赋给左边
            right -= 1  # 往左边走一步
            # 要切记while是一个循环，当满足循环条件是，循环体会一直执行，直到跳出循环才会执行下一步
        li[left] = li[right]
        while left < right and li[left] <= tmp:  # 从左边找比tmp大的数，如果找到了，则把这个大的数赋给右边
            left += 1  # 往右走一步
        li[right] = li[left]
    li[left] = tmp  # tmp归位
    return left  # 或者right，因为这时候left == right


# 然后递归partition进行快排
def _quick_sort(li, left, right):
    if left < right:  # 至少有两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@call_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


# 与冒泡排序做一个时间上的比较
@call_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:  # 要判断
            return li
    return li


li = [random.randint(0, 10000) for i in range(10000)]

# 为了让两种排序算法同时执行，使用深拷贝
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

# li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(li=li1)
# print(li1)
bubble_sort(li=li2)
# print(li2)

"""
    quick_sort running time is 0.01900005340576172.
    bubble_sort running time is 6.826030492782593.
"""