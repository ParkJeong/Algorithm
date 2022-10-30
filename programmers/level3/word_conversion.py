# 두 개의 단어 begin, target과 단어의 집합 words가 있다.
# begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾는다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
# 2. words에 있는 단어로만 변환할 수 있다.
# 예를 들어 begin이 "hit", target가 "cog"
# words가 ["hot","dot","dog","lot","log","cog"]
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
import sys


def is_changeable(before, after):
    count = 0
    for idx in range(len(before)):
        if before[idx] != after[idx]:
            count += 1
    return True if count == 1 else False


def dfs(now, target, words, visited, result):
    step = max(visited)
    if now == target:
        result.append(step)
        return
    elif step > len(words):
        result.append(0)
        return

    for idx in range(len(words)):
        if is_changeable(now, words[idx]) and visited[idx] == 0:
            new_visited = visited[:]
            new_visited[idx] = max(visited) + 1
            dfs(words[idx], target, words, new_visited, result)


def solution(begin, target, words):
    sys.setrecursionlimit(10 ** 6)
    visited = [0 for _ in range(len(words))]
    result = []
    dfs(begin, target, words, visited, result)
    answer = 0 if len(result) == 0 else min(result)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]	))


from collections import deque


def get_changeable(now, words):
    for word in words:
        count = 0
        for before, after in zip(now, word):
            if before != after:
                count += 1
        if count == 1:
            yield word


def bfs(begin, target, words):
    visited = dict()
    queue = deque()

    visited[begin] = 0
    queue.append(begin)

    while len(queue) > 0:
        now = queue.popleft()
        if now == target:
            return visited[now]

        for word in get_changeable(now, words):
            if word not in visited.keys():
                visited[word] = visited[now] + 1
                queue.append(word)
    return 0





def solution(begin, target, words):
    return bfs(begin, target, words)