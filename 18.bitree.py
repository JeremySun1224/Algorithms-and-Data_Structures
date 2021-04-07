# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/7 -*-

"""二叉树的创建与遍历"""


class BiTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


def pre_order(root):
    """前序遍历"""
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


if __name__ == '__main__':
    a = BiTreeNode('A')
    b = BiTreeNode('B')
    c = BiTreeNode('C')
    d = BiTreeNode('D')
    e = BiTreeNode('E')
    f = BiTreeNode('F')
    g = BiTreeNode('G')

    e.lchild = a
    e.rchild = g
    a.rchild = c
    c.lchild = b
    c.rchild = d
    g.rchild = f

    root = e

    # 创建二叉树
    # print(root.lchild.rchild.data)

    # 遍历二叉树
    pre_order(root=root)
