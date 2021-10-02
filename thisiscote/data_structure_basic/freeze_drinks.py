from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1 ,0]


def bfs(graph, x, y, visited, n, m):
  visited[y][x] = True

  queue = deque()
  queue.append([x,y])
  while queue:
    p = queue.popleft()
    for i in range(4):
      nx = p[0] + dx[i]
      ny = p[1] + dy[i]
      if nx >= 0 and nx <= m - 1 and ny >= 0 and ny <= n - 1 and not visited[ny][nx] and graph[ny][nx] == '0':
        queue.append([nx, ny])
        visited[ny][nx] = True

# n, m = map(int, input().split())

# freeze = []
# for _ in range(n):
#   freeze.append(input())

n, m = 15, 14
freeze = list()
freeze.append('00000111100000')
freeze.append('11111101111110')
freeze.append('11011101101110')
freeze.append('11011101100000')
freeze.append('11011111111111')
freeze.append('11011111111100')
freeze.append('11000000011111')
freeze.append('01111111111111')
freeze.append('00000000011111')
freeze.append('01111111111000')
freeze.append('00011111111000')
freeze.append('00000001111000')
freeze.append('11111111110011')
freeze.append('11100011111111')
freeze.append('11100011111111')
visited = [[False] * m for _ in range(n)]

count = 0
for x in range(m):
  for y in range(n):
    if not visited[y][x] and freeze[y][x] == '0':
      bfs(freeze, x, y, visited, n, m)
      count += 1

print(count)
