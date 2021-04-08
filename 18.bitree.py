# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/7 -*-

"""二叉树的创建与遍历"""

from collections import deque


class BiTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


def pre_order(root):
    """前序遍历"""
    if root:
        print(root.data, end=',')  # 先访问根节点
        pre_order(root.lchild)  # 再递归左子树
        pre_order(root.rchild)  # 最后递归右子树


def in_order(root):
    """中序遍历"""
    if root:
        in_order(root.lchild)  # 先递归左子树
        print(root.data, end=',')  # 再访问根节点
        in_order(root.rchild)  # 最后递归右子树


def post_order(root):
    """后序遍历"""
    if root:
        post_order(root.lchild)  # 先递归左子树
        post_order(root.rchild)  # 再递归右子树
        print(root.data, end=',')  # 最后访问根节点


def level_order(root):
    """层次遍历"""
    queue = deque()
    queue.append(root)  # 先让root进队
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()  # 出队
        print(node.data, end=',')

        # 检查是否有左右孩子，有则进队
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


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
    # pre_order(root=root)  # 前序遍历
    # in_order(root=root)  # 中序遍历
    # post_order(root=root)  # 后序遍历
    level_order(root=root)  # 层次遍历
