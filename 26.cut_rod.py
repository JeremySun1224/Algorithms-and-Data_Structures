# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/10 -*-

"""递归解钢条切割问题"""

from time import time


def cal_time(func):
    def wrapper(*arg, **kwargs):
        t1 = time()
        result = func(*arg, **kwargs)
        t2 = time()
        print(f'{func.__name__} running time: {t2 - t1}')
        return result

    return wrapper


price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


def cut_rod_recurrent_1(p, n):
    """两边同时切割"""
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurrent_1(p, i) + cut_rod_recurrent_1(p, n - i))
        return res


@cal_time
def c1(p, n):
    return cut_rod_recurrent_1(p, n)


def cut_rod_recurrent_2(p, n):
    """左边不切割，只切割右边"""
    if n == 0:
        return 0
    else:
        res = 0  # 初始化最大收益，在for循环的计算中，还会有p[i]做基础
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recurrent_2(p, n - i))  # p[i]表示左边不切割的部分
        return res


@cal_time
def c2(p, n):
    return cut_rod_recurrent_2(p, n)


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
    print(c1(p=price, n=20))
    print(c2(p=price, n=20))
