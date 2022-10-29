# 7시 48분 ~ 8시 30분
# 1000, 1000
# 1_000_000_000
#    20_000_000
#
import sys

DIRECTION_X = [0, 1, 0, -1]
DIRECTION_Y = [-1, 0, 1, 0]
DIRECTION_NUM = 4


col_num, row_num = map(int, sys.stdin.readline().split())

box = [[] * _ for _ in range(row_num)]
tomatoes = []

for row in box:
    row.extend(list(map(int, sys.stdin.readline().split())))

for row_idx in range(row_num):
    for col_idx in range(col_num):
        if box[row_idx][col_idx] == 1:
            tomatoes.append((col_idx, row_idx))

result = -1
while len(tomatoes) > 0:
    now_tomates = tomatoes[:]
    tomatoes = []
    for now_tomato in now_tomates:
        for idx in range(DIRECTION_NUM):
            new_tomato_col = now_tomato[0] + DIRECTION_X[idx]
            new_tomato_row = now_tomato[1] + DIRECTION_Y[idx]
            if 0 <= new_tomato_row < row_num and 0 <= new_tomato_col < col_num and box[new_tomato_row][new_tomato_col] == 0:
                box[new_tomato_row][new_tomato_col] = 1
                tomatoes.append((new_tomato_col, new_tomato_row))
    result += 1

# box가 모두 1인지 확인
for row in box:
    for cell in row:
        if cell == 0:
            result = -1

print(result)