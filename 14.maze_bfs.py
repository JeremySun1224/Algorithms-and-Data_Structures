# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/6 -*-

"""用队列解决迷宫问题——广度优先搜索，这样找到的路径一定是最短的"""

from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def print_path(path):
    real_path = []
    i = len(path) - 1
    while i >= 0:
        real_path.append(path[i][0: 2])
        i = path[i][2]
    real_path.reverse()
    for node in real_path:
        print(node)
    return real_path


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    path = []  # 谁带它进来的，记录下标
    # append()表示从右边入队，所以接下来的出队需要用popleft()左边出队。
    queue.append((x1, y1, -1))  # 入队-1表示起点位置是谁带它进来的，由于是起点位置，故直接写为-1
    while len(queue) > 0:  # 当队列非空时循环，只要队空的话说明没有路径
        cur_node = queue.popleft()  # popleft()表示从左边出队
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            print_path(path)
            return True
        for _dir in dirs:
            next_node = _dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:  # 说明这个格子可以走，那么入队
                queue.append((next_node[0], next_node[1], len(path) - 1))  # len(path)-1表示存储cur_node在当前位置的下标
                maze[next_node[0]][next_node[1]] = 2  # 标记为已走过
    else:
        print('没有路')
        return False

if __name__ == '__main__':
    maze_path_queue(1, 1, 8, 8)