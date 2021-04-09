# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/9 -*-

"""贪心解字符串拼接问题"""

from functools import cmp_to_key


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))  # 整数转化成字符串
    li.sort(key=cmp_to_key(mycmp=xy_cmp))  # cmp_to_key()在list中的工作机制就是将列表中的元素去两两比较，当cmp返回是正数时 交换两元素
    return ''.join(li)


if __name__ == '__main__':
    l = [32, 94, 128, 1286, 6, 71]
    print(number_join(li=l))
