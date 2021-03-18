# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/12/28 -*-

def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j  # 找到最小的位置后和无序区第一个值进行交换，此时无序区第一个值为i
            # li[j], li[min_loc] = li[min_loc], li[j]  # 如果写j，由于min_loc = j，所以并没有发生交换
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]  # 如果找到比当前min_loc位置更小的数， 则把这个数的位置和最小位置进行调换
    return li


li = [5, 3, 6, 7, 9, 1, 8, 4]
print(select_sort(li=li))
