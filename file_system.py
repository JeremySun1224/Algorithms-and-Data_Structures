# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/7 -*-

"""用树结构实现文件系统"""


class Node(object):
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree(object):
    def __init__(self):
        self.root = Node(name='/')
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'

        node = Node(name=name)  # 创建文件夹
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'

        if name == '../':
            self.now = self.now.parent
            return None

        for child in self.now.children:
            if child.name == name:
                self.now = child  # 切换目录
                return None
        raise ValueError('Invalid Dir.')


if __name__ == '__main__':
    tree = FileSystemTree()
    tree.mkdir('var/')
    tree.mkdir('bin/')
    tree.mkdir('usr/')

    tree.cd('bin/')
    tree.mkdir('python/')
    tree.cd('../')
    print(tree.root.children)
    print(tree.ls())
