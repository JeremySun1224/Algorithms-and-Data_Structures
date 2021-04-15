# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/21 -*-

"""归并排序"""

import random


def merge(li, low, mid, high):
    """归并"""
    i = low  # 第一段的第一个元素
    j = mid + 1  # 第二段的第一个元素
    li_tmp = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    # while执行完，肯定有一部分，另一部分还有数，那么就要继续循环取出剩下的数
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    # 把li_tmp的值写回li
    li[low: high + 1] = li_tmp  # 切片可以往回写
    return li


def merge_sort(li, low, high):
    """归并排序"""
    if low < high:  # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(li=li, low=low, high=mid)
        merge_sort(li=li, low=mid + 1, high=high)
        merge(li=li, low=low, mid=mid, high=high)
    return li


if __name__ == '__main__':
    li = list(range(100))
    random.shuffle(li)
    print(f'排序前: {li}')
    merge_sort(li=li, low=0, high=len(li) - 1)
    print(f'排序后: {li}')
