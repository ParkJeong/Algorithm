from sys import stdin
from collections import deque
"""
deq = deque()
dqe.append()
deq.popleft()

col이 x좌표
row가 y좌표다
"""
input = stdin.readline
test_case_num = int(input().strip())

DIRECTION_X = [0, 1, 0, -1]
DIRECTION_Y = [-1, 0, 1, 0]


def count_worm(cabbage_map, col, row):
    queue = deque()
    count = 0
    for y in range(row):
        for x in range(col):
            if cabbage_map[y][x] == 1:
                queue.append((x, y))
                cabbage_map[y][x] = 0
                count += 1
                while len(queue) > 0:
                    temp_x, temp_y = queue.popleft()
                    for idx in range(4):
                        new_x = temp_x + DIRECTION_X[idx]
                        new_y = temp_y + DIRECTION_Y[idx]
                        if 0 <= new_x < col and 0 <= new_y < row and cabbage_map[new_y][new_x] == 1:
                            queue.append((new_x, new_y))
                            cabbage_map[new_y][new_x] = 0
    return count


for _ in range(test_case_num):
    col, row, cabbage_num = map(int, input().split())

    cabbage_map = [[0] * col for _ in range(row)]
    for _ in range(cabbage_num):
        x, y = map(int, input().split())
        cabbage_map[y][x] = 1
    print(count_worm(cabbage_map, col, row))



