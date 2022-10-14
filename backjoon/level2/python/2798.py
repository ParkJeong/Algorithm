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



# 순열 조합
# combinations_with_replacement() 중복조합
from itertools import combinations, combinations_with_replacement

CARD_NUM, TARGET_NUM = map(int, input()).split()
CARD_LIST = list(map(int, input().split()))
sum = 0

for candidate_card_list in combinations(CARD_LIST, 3):
    temp_sum = sum(candidate_card_list)
    if sum < temp_sum <= TARGET_NUM:
        sum = temp_sum

print(sum)
