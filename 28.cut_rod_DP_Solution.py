# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/10 -*-

"""重构解"""


def cut_rod_extend(p, n):
    """重构解"""
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0  # 收益的最大值
        res_s = 0  # 收益最大时对应方案的左边不切割部分的长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    """输出最优切法"""
    r, s = cut_rod_extend(p, n)
    ans = []  # 存储最优切法
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
    print(f'最大收益的切割方案为：{cut_rod_solution(p=price, n=20)}')  # 最大收益的切割方案为：[2, 6, 6, 6]
