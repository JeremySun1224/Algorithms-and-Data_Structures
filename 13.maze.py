# -*- coding: utf-8 -*-
# -*- author: JeremySun -*-
# -*- dating: 21/4/6 -*-

"""用栈解决迷宫问题，思想为深度优先搜索，也可以称为回溯法。但是使用栈的方法不能保证所走路径是最短的"""

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


def maze_path(x1, y1, x2, y2):
    stack = []  # 空栈
    stack.append((x1, y1))  # 最开始栈存的是起点的坐标
    # 接下来只要栈不空就循环
    while len(stack) > 0:
        cur_node = stack[-1]  # 当前的节点
        # 判断当前节点是否是终点
        if cur_node[0] == x2 and cur_node[1] == y2:
            for p in stack:
                print(p)
            return True
        # 从四个方向寻找
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            # 如果下一个节点能走
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)  # 入栈
                maze[next_node[0]][next_node[1]] = 2  # 走过的格子赋值为2
                break
        else:  # 如果一个方向都找不到了，就该回退了，即出栈
            maze[next_node[0]][next_node[1]] = 2  # 2表示已经走过
            stack.pop()  # 栈顶出栈
    else:  # 栈空
        print('没有路')
        return False


if __name__ == '__main__':
    maze_path(1, 1, 8, 8)
