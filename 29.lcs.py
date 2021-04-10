# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/10 -*-

"""动态规划解最长公共子序列问题"""


def lcs_length(x, y):
    """返回最长公共子序列的长度"""
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:  # i,j位置上的字符匹配时，来自于左上方+1
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


if __name__ == '__main__':
    print(lcs_length('ABCBDAB', 'BDCABA'))