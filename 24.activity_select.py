# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/9 -*-

"""贪心解活动选择问题"""


def activity_select(a):
    a.sort(key=lambda x: x[1])  # 需要保证传入的活动集a是排序好的
    res = [a[0]]
    for i in range(1, len(a)):
        # 如果当前活动的开始时间小于等于最后一个入选活动的结束时间则不冲突
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res


if __name__ == '__main__':
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    print(activity_select(a=activities))
