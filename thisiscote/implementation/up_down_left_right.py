# 2트
import sys
import time

start_time = time.time()
#########################
n = int(sys.stdin.readline())

moves = sys.stdin.readline().split()
start_x = 1
start_y = 1
for move in moves:
    if move == "R" and start_x < n:
        start_x += 1
    if move == "D" and start_y < n:
        start_y += 1
    if move == "L" and start_x > 1:
        start_x -= 1
    if move == "U" and start_y > 1:
        start_y -= 1

print(start_x, start_y)
#######################
end_time = time.time()
print(f"time:{end_time - start_time}")



len = int(input())
moveList = input().split() # moveList

# 답안
n = len
x, y = 1, 1
plans = moveList
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    x, y = nx, ny



# 내 풀이

rowLoc = 1
colLoc = 1

for move in moveList:
  if move == 'R' and rowLoc < len:
    rowLoc += 1
  elif move == 'L' and rowLoc > 1:
    rowLoc -= 1
  elif move == 'U' and colLoc > 1:
    colLoc -= 1
  elif move == 'D' and colLoc < len:
    colLoc += 1
print(colLoc, rowLoc)
