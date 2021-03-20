# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/18 -*-

"""堆排序"""

import random


def sift(li, low, high):
    """
    大根堆向下调整函数
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置，大于high就越界了
    :return:
    """
    # 需要一个i和j分别指向当前层和下一层(即孩子节点)
    i = low
    j = 2 * i + 1  # 由父节点找左孩子节点
    tmp = li[low]  # 把堆顶存起来
    # 接下来需要进入循环去判断，这个tmp是否属于这一层
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # 把j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            # 更新i，相当于往下看一层
            i = j
            j = 2 * i + 1
        else:  # tmp更大，把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级领导的位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子结点上


def heap_sort(li):
    n = len(li)
    """构造堆"""
    for i in range((n - 2) // 2, -1, -1):  # 倒序，for循环后建堆完成
        # i表示构造堆的时候调整的部分的根的下标
        sift(li=li, low=i, high=n - 1)
    """挨个出数"""
    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li=li, low=0, high=i - 1)  # i-1是新的high


if __name__ == '__main__':
    li = [i for i in range(100)]
    random.shuffle(li)
    print(f'排序前: {li}')
    heap_sort(li=li)
    print(f'排序后: {li}')
