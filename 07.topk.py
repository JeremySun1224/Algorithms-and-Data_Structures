# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/3/20 -*-

"""堆排序的应用: TopK问题"""

import random


def sift(li, low, high):
    """
    小根堆向下调整函数
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
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # 把j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            # 更新i，相当于往下看一层
            i = j
            j = 2 * i + 1
        else:  # tmp更大，把tmp放到i的位置上
            break
        li[i] = tmp


def top_k(li, k):
    """
    top_k问题
    :param li: 要排序的列表
    :param k: 取li的前k个数
    :return: li
    """
    heap = li[0: k]
    # 1.建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(li=heap, low=i, high=k - 1)
    # 2.遍历
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:  # 如果要比较的数大于堆顶的数
            heap[0] = li[i]
            sift(li=heap, low=0, high=k - 1)
    # 3.出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]  # 应该从heap上去改，因为heap这时候是堆
        sift(li=heap, low=0, high=i - 1)
    return heap


if __name__ == '__main__':
    li = list(range(1000))
    random.shuffle(li)
    print(top_k(li=li, k=10))
