from collections import deque

def bfs(now, total):
    global result

    if now >= MAX_DEPTH:
        return

    for idx in range(MAX_DEPTH - now):
        bfs(now + idx + 1, total)
        total += CARD_LIST[now]
        if total <= TARGET_NUM:
            result = total if result < total else result

        bfs(now + idx + 1, total)


CARD_NUM, TARGET_NUM = map(int, input().split())

CARD_LIST = list(map(int, input().split()))
MAX_DEPTH = len(CARD_LIST)
result = 0

bfs(0, 0)

print(result)