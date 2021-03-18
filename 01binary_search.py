# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/12/27 -*-

"""
    二分查找
"""

# 这是错误写法，根本找不到需要查找数字的索引啊
# def binary_search(li, val):
#     left = 0
#     right = len(li)
#     while left <= right:
#         mid = (left + right) // 2
#         if mid == val:
#             return mid
#         elif mid < val:
#             left = mid + 1
#         else:
#             right = mid - 1
#     else:
#         return None

from call_time import *


@call_time
def linear_search(li, val):
    for idx, i in enumerate(li):
        if i == val:  # 不能用i，应该使用索引去找到对应的值
            return idx
        # else:
        #     return None  # 这样写的话，测试一个值后代码就结束了
    else:
        return None


@call_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1  # 因为python是零索引，所以需要减1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None


if __name__ == '__main__':
    li = list(range(1000000))
    val = 389000
    print(linear_search(li=li, val=val))
    print(binary_search(li=li, val=val))
    """
    linear_search running time is 0.017003774642944336.
    389000
    binary_search running time is 0.0.
    389000
    """
