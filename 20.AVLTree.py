# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/9 -*-

"""AVL树的旋转实现"""


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
        """递归查询"""
        if not node:
            return None
        if node.data < val:
            return self.query_recurrent(node.rchild, val)
        elif node.data > val:
            return self.query_recurrent(node.lchild, val)
        else:
            return None

    def query_non_recurrent(self, val):
        """非递归查询"""
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        """情况1：node是叶子节点"""
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = None
        else:  # node是它父亲的右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        """情况2.1：node只有一个左孩子"""
        if not node.parent:  # 判断是否是根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # node是它父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        """情况2.2：node只有一个右孩子"""
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild  # node.parent.lchild这里指的是树中连接树的箭头
            node.rchild.parent = node.parent  # node.rchild.parent这里指的是树中连接树的箭头
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        """删除操作"""
        if self.root:  # 不是空树
            node = self.query_non_recurrent(val)
            if not node:  # 不存在
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:  # 如果它没有右孩子，那么就一定有左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # 只有一个右孩子
                self.__remove_node_22(node)
            else:
                """
                情况3：两个孩子都有:
                    1).先找右子树最小的节点，如果有就一直往左找，直到没有为止
                    2).把找到的节点替换到当前的节点
                    3).删除min_node
                """
                min_node = node.rchild
                while min_node.lchild:  # min_node有左孩子
                    min_node = min_node.lchild  # 找到了右子树里最小的节点
                node.data = min_node.data  # 把找到的节点替换到当前的节点
                # 删除min_node
                if min_node.rchild:
                    # self.__remove_node_22(node)  # 错误写法，这里需要移除的是最小节点
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

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


class AVLNode(BiTreeNode):
    def __init__(self, data):
        super(AVLNode, self).__init__(data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        super(AVLTree, self).__init__(li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
