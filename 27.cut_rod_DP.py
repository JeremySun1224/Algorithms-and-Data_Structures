# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/10 -*-

"""
动态规划解钢条切割问题
    1、递归算法由于重复求解相同子问题，效率较低。
    2、动态规划思想：
        1）每个子问题只求解一次，保存求解结果；
        2）之后需要此问题时，只需查找保存的结果。
"""
from time import time


def cal_time(func):
    def wrapper(*arg, **kwargs):
        t1 = time()
        result = func(*arg, **kwargs)
        t2 = time()
        print(f'{func.__name__} running time: {t2 - t1}')
        return result

    return wrapper


def cut_rod_recurrent_2(p, n):
    """左边不切割，只切割右边：O(2^n)"""
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


@cal_time
def cut_rod_dp(p, n):
    """动态规划：O(n^2)"""
    r = [0]  # 存储子问题的结果
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)  # 暂存
    return r[n]


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
    print(f'最大收益为：{c2(p=price, n=20)}')
    print(f'最大收益为：{cut_rod_dp(p=price, n=20)}')
    """
    c2 running time: 0.39551401138305664
    最大收益为：56
    cut_rod_dp running time: 0.0
    最大收益为：56
    """
