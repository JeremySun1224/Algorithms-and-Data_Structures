# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/9 -*-

"""求斐波那契数列的第n项"""


def fibonacci(n):
    """递归写法，进行了大量子问题的重复计算，所以递归写法效率低"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_non_recurrent(n):
    """
    非递归写法，可以理解成动态规划的思想：
        1.最优子结构，即要解决某个问题，只需解决这个问题的某个子问题即可。如fibonacci数列的递推式
        2.重复子问题
    """
    f = [0, 1, 1]  # 为了让下标同步，故f从0开始写
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


if __name__ == '__main__':
    # print(fibonacci(50))
    print(fibonacci_non_recurrent(50))
