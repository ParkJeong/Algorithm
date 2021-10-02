from collections import deque

def bfs(graph, start, visited):
  queue = deque()
  queue.append(start)
  visited[start] = True

  while queue:
    now = queue.popleft()
    print(start, end=' ')

    for next in graph[now]:
      if not visited[next]:
        queue.append(next)
        visited[next] = True


graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
]

visited = [False] * 9
bfs(graph, 1, visited)
