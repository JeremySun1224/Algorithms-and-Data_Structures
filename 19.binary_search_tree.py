# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/8 -*-

"""二叉搜索树"""

import random


class BiTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST(object):
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_non_recurrent(val)

    def insert_recurrent(self, node, val):
        """
        递归插入
        :param node: 递归的查到哪个节点
        :param val: 要插入的值
        :return: node
        """
        if not node:  # 如果node是空
            node = BiTreeNode(val)  # 直接插入。BiTreeNode(val)指的是把val变成一个node
        elif val < node.data:
            node.lchild = self.insert_recurrent(node.lchild, val)  # 递归地调用左孩子
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert_recurrent(node.rchild, val)  # 递归地调用右孩子
            node.rchild.parent = node
        return node

    def insert_non_recurrent(self, val):
        """
        非递归插入
        :param val:
        :return:
        """
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query_recurrent(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query_recurrent(node.rchild, val)
        elif node.data > val:
            return self.query_recurrent(node.lchild, val)
        else:
            return None

    def query_non_recurrent(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def pre_order(self, root):
        """前序遍历"""
        if root:
            print(root.data, end=',')  # 先访问根节点
            self.pre_order(root.lchild)  # 再递归左子树
            self.pre_order(root.rchild)  # 最后递归右子树

    def in_order(self, root):
        """中序遍历"""
        if root:
            self.in_order(root.lchild)  # 先递归左子树
            print(root.data, end=',')  # 再访问根节点
            self.in_order(root.rchild)  # 最后递归右子树

    def post_order(self, root):
        """后序遍历"""
        if root:
            self.post_order(root.lchild)  # 先递归左子树
            self.post_order(root.rchild)  # 再递归右子树
            print(root.data, end=',')  # 最后访问根节点


if __name__ == '__main__':
    li = list(range(0, 500, 2))
    random.shuffle(li)

    tree = BST(li=li)
    # 插入
    # tree.pre_order(tree.root)
    # print('')
    # tree.in_order(tree.root)
    # print('')
    # tree.post_order(tree.root)

    # 查询
    print(tree.query_non_recurrent(val=3))