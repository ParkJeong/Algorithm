import sys
from itertools import product
from collections import deque

DIRECTION_X = [0, 1, 0, -1]
DIRECTION_Y = [-1, 0, 1, 0]
DIRECTION = 4


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def plant_cabbage(farm, cabbage_num):
    for _ in range(cabbage_num):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        farm[y][x] = 1


def get_farm(width, height):
    farm = [[0] * width for _ in range(height)]
    return farm


def move_to_other_cabbage(farm, pos):
    height = len(farm)
    width = len(farm[0])
    queue = deque()
    queue.append(pos)
    farm[pos.y][pos.x] = 0
    while len(queue) > 0:
        now = queue.popleft()
        for idx in range(DIRECTION):
            new_x = now.x + DIRECTION_X[idx]
            new_y = now.y + DIRECTION_Y[idx]
            if (0 <= new_x < width and 0 <= new_y < height) and farm[new_y][new_x] == 1:
                farm[new_y][new_x] = 0
                new_pos = Point(new_x, new_y)
                queue.append(new_pos)


def is_cabbage_area(farm, pos: Point):
    x = pos.x
    y = pos.y
    if farm[y][x] == 0:
        return False

    move_to_other_cabbage(farm, pos)
    return True


test_cases_num = int(sys.stdin.readline())

for _ in range(test_cases_num):
    width, height, cabbage_num = map(int, sys.stdin.readline().rstrip().split())
    count = 0
    farm = get_farm(width, height)

    plant_cabbage(farm, cabbage_num)

    for row, col in product(range(width), range(height)):
        pos = Point(row, col)
        count += 1 if is_cabbage_area(farm, pos) else 0
    print(count)