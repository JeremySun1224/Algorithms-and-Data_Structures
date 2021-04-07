# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/6 -*-

"""链表的创建与遍历"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


def create_linklist_head(li):
    """头插法"""
    head = Node(item=li[0])
    # 接下来就是一直往头节点里插入元素
    for element in li[1:]:
        node = Node(item=element)  # 创建新节点
        node.next = head  # 1.连接节点
        head = node  # 2.把新插入的那个节点作为新的头节点
    return head


def create_linklist_tail(li):
    """尾插法"""
    head = Node(item=li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node  # 让新的node成为tail
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end='->')
        lk = lk.next  # 查看后一节点


if __name__ == '__main__':
    lk_head = create_linklist_head(li=[1, 2, 3])
    print_linklist(lk_head)
    print()
    lk_tail = create_linklist_tail(li=[1, 2, 4, 5, 9])
    print_linklist(lk_tail)
