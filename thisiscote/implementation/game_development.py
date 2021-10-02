# 답안

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    diretion = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dx[direction]

  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0
print(count) 
# 내 답안

n, m = map(int, input().split())
x, y, direc = map(int, input().split())

game_map = []
visited = [[0] * m for _ in range(n)]

direc_x = [0, 1, 0, -1]
direc_y = [-1, 0, 1, 0]
for row in range(n):
  game_map.append(list(map(int, input().split())))

visited[x][y] = True

# 0 -> 3
# 1 -> 0
# 2 -> 1
# 3 -> 2
move = 0;
while True:
  limit_direc = 4
  while limit_direc:
    direc = 3 if direc == 0 else direc - 1
    limit_direc -= 1
    nx, ny = x + direc_x[direc], y + direc_y[direc]
    if nx >= 0 and nx <= m - 1 and ny >= 0 and ny <= n - 1 and not visited[nx][ny] and game_map[nx][ny] == 0:
      break
  if limit_direc == 0:
    nx, ny = x - direc_x[direc], y - direc_y[direc]
    if game_map[nx][ny] == 1:
      break
  x, y = nx, ny
  visited[x][y] = True
  move += 1
print(move)    
