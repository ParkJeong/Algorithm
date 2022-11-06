# ROR 게임은 두 팀으로 나누어서 진행
# 상대 팀 진영을 먼저 파괴하면 이김
# 상대 진영에 빨리 도착해야함
# 5X5 크기 맵
# 나는 1, 1에 있고 상대는 5,5있다.
# 검은 색은 벽으로 갈 수 없는 길
# 흰 색은 갈 수 있는 길
# 캐릭터는 동서남북으로 이동가능
# 게임 맵을 벗어날 수는 없다.
# 상대 팀 진영에 도착하기 위해 지나가야 하는 칸의 최솟값
# 도착할 수 없는 경우 -1

# 제한 사항
# 1 <= 가로 N, 세로 M<= 100
# 가로 세로는 같을 수 있지만 1X1은 없다.
# 0은 벽, 1은 지나갈 수 있는 자리
# 시작 위치 1,1
# 상대방은 N, M에 있다.


def bfs(maps, visited, width, height):
    from collections import deque
    DIRECTION_X = [1, 0, -1, 0]
    DIRECTION_Y = [0, 1, 0, -1]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        now_x, now_y = queue.popleft()

        if now_x == width - 1 and now_y == height - 1:
            return visited[now_y][now_x]

        for direction_x, direction_y in zip(DIRECTION_X, DIRECTION_Y):
            new_x = now_x + direction_x
            new_y = now_y + direction_y

            if 0 <= new_x < width and 0 <= new_y < height and maps[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                visited[new_y][new_x] = visited[now_y][now_x] + 1
                queue.append((new_x, new_y))
    return -1



def solution(maps):
    if len(maps) == 1 and len(maps[0]) == 1:
        return 1
    import sys
    sys.setrecursionlimit(10 ** 8)
    # 맵 그래프 만들기
    # 이미 주어짐

    # 초기상태 만들기
    # 방문 검색을 위한 데이터 만들기
    height = len(maps)
    width = len(maps[0])
    visited = [[0] * width for _ in range(height)]
    # bfs 로 최단거리 찾기
    # answer = bfs(maps, visited, width, height)
    DIRECTION_X = [1, 0, -1, 0]
    DIRECTION_Y = [0, 1, 0, -1]

    def dfs(x, y, step):
        if maps[height - 1][width - 1] != 1 and step >= maps[height - 1][width - 1]:
            return
        maps[y][x] = step

        for direction_x, direction_y in zip(DIRECTION_X, DIRECTION_Y):
            new_x = x + direction_x
            new_y = y + direction_y
            if 0 <= new_x < width and 0 <= new_y < height and maps[new_y][new_x] != 0 and \
                    (maps[new_y][new_x] == 1 or maps[new_y][new_x] > step + 1):
                dfs(new_x, new_y, step + 1)

    dfs(0, 0, 1)
    answer = -1 if maps[height - 1][width - 1] == 1 else maps[height - 1][width - 1]
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))


##############################################
# import sys
#
# DIRECTION_X = [0, 1, 0, -1]
# DIRECTION_Y = [-1, 0, 1, 0]
# DIRECTION_NUM = 4
#
#
# def find_the_shortest_path(maps, n, m, now_x, now_y, result, visited):
#     if now_x == n-1 and now_y == m - 1:
#         return visited[now_y][now_x]
#
#     for direction_idx in range(DIRECTION_NUM):
#         next_x = now_x + DIRECTION_X[direction_idx]
#         next_y = now_y + DIRECTION_Y[direction_idx]
#
#         if 0 <= next_x <= n-1 and 0 <= next_y <= n-1 and maps[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
#             if visited[next_y][next_x] != 0:
#                 visited[next_y][next_x] = min(visited[now_y][now_x] + 1, visited[next_y][next_x])
#             else:
#                 visited[next_y][next_x] = visited[now_y][now_x] + 1
#             result.append(find_the_shortest_path(maps, n, m, next_x, next_y, result, visited))
#
#     return -1
#
# from collections import deque
#
# def solution(maps):
#     height = len(maps)
#     width = len(maps[0])
#     visited = [[0] * width for _ in range(height)]
#     visited[0][0] = 1
#
#     queue = deque()
#     queue.append((0, 0))
#
#     while len(queue) > 0:
#         now_x, now_y = queue.popleft()
#
#         if now_x == width - 1 and now_y == height - 1:
#             break
#
#         for direction_x, direction_y in zip(DIRECTION_X, DIRECTION_Y):
#             new_x = now_x + direction_x
#             new_y = now_y + direction_y
#
#             if 0 <= new_x < width and 0 <= new_y < height and maps[new_y][new_x] and visited[new_y][new_x] == 0:
#                 visited[new_y][new_x] = visited[now_y][now_x] + 1
#                 queue.append((new_x, new_y))
#
#
#     return visited[height - 1][width - 1]
#
#     # find_the_shortest_path(maps, len(maps), len(maps[0]), 0, 0, answer, visited)
#
# print(
#     solution(
#         [
#             [1, 0, 1, 1, 1],
#             [1, 0, 1, 0, 1],
#             [1, 0, 1, 1, 1],
#             [1, 1, 1, 0, 1],
#             [0, 0, 0, 0, 1]
#         ]
#     )
# )
