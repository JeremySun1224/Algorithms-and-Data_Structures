# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 20/12/28 -*-

# def insert_sort(li):
#     for i in range(1, len(li)):
#         for j in range(0, i):
#             tmp = li[i]
#             while j >= 0 and li[j] > li[i]:
#                 li[j + 1] = li[j]
#                 li[j + 1] = tmp
#     return li

# def insert_sort(li):
#     for i in range(1, len(li)):
#         for j in range(0, i):
#             while j >= 0 and li[j] > li[i]:
#                 li[j + 1] = li[j]
#                 li[j] = li[i]
#                 j = j - 1
#     return li

def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到的牌
        j = i - 1  # j表示手里的牌
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1  # 每次比较后，需要把j往前移一位
        li[j + 1] = tmp
    return li


li = [5, 3, 6, 7, 9, 1, 8, 4]
print(insert_sort(li=li))
