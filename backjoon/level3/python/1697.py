from collections import deque


def solution(n, k, visited):
    queue = deque()

    queue.append(n)

    while queue:
        now = queue.popleft()
        if now == k:
            return visited[now]

        for new_now in [now + 1, now - 1, now * 2]:
            if 0 <= new_now <= 100_000 and visited[new_now] == 0:
                visited[new_now] = visited[now] + 1
                queue.append(new_now)

        # if now + 1 <= 100_000 and not visited[now + 1]:
        #     visited[now + 1] = True
        #     queue.append((now + 1, step + 1))
        # if now > 0 and not visited[now - 1]:
        #     visited[now - 1] = True
        #     queue.append((now - 1, step + 1))
        # if now * 2 <= 100_000 and not visited[now * 2]:
        #     visited[now * 2] = True
        #     queue.append((now * 2, step + 1))


n, k = map(int, open(0).readline().rstrip().split())
# visited = [False for _ in range(100_001)]
visited = [0 for _ in range(100_001)]
result = solution(n, k, visited)
print(result)
