# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/7 -*-

"""哈希表的实现与应用"""


class LinkList(object):
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)  # 先创建节点
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s  # 先把其与链表尾部接起来，然后复制
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):  # self是可迭代的
        return '<<' + ','.join(map(str, self)) + '>>'

    class Node(object):
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator(object):
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self  # 返回自身


class HashTable(object):
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for _ in range(size)]  # 用拉链法解决哈希冲突

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)  # 首先计算哈希值
        if self.find(k):  # 去重
            print('Duplicated Insert.')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


if __name__ == '__main__':
    # lk = LinkList([1, 2, 3, 4, 5])
    # print(lk)
    ht = HashTable()
    ht.insert(0)
    ht.insert(1)
    # ht.insert(0)  # Duplicated Insert.
    ht.insert(3)
    ht.insert(102)
    ht.insert(508)

    print(ht.find(3))  # True
    print(ht.find(10))  # False
    print(','.join(map(str, ht.T)))

    """<<0>>,<<1,102>>,<<>>,<<3,508>>..."""
