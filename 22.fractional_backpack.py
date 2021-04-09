# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/9 -*-

"""贪心解分数背包问题"""


def fractional_backpack(g, w):
    m = [0 for _ in range(len(g))]  # 每种商品怎么拿
    total_v = 0
    for idx, (price, weight) in enumerate(g):
        if w >= weight:
            m[idx] = 1
            total_v += price
            w -= weight
        else:
            m[idx] = w / weight
            total_v += m[idx] * price
            break  # 这个时候包已经满了，可以直接跳出
    return total_v, m


if __name__ == '__main__':
    goods = [(60, 10), (120, 30), (100, 20)]  # 每个商品用元组表示（价格，重量）
    goods.sort(key=lambda x: x[0] / x[1], reverse=True)  # 价格/重量=单位价值
    print(fractional_backpack(g=goods, w=50))
