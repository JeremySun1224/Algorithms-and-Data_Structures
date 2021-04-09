# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/9 -*-

"""贪心解找零问题"""


def change(types, n):
    num = [0 for _ in range(len(types))]
    types_sorted = sorted(types, reverse=True)
    for idx, money in enumerate(types_sorted):  # 把num和money_types通过共同的索引联系起来
        num[idx] = n // money  # 需要不同种类的钱的张数
        n = n % money  # 当前余额
    return num, n


if __name__ == '__main__':
    money_types = [100, 50, 20, 10, 5, 1]
    print(change(types=money_types, n=376))
