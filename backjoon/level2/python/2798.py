import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())

cards = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for candidate in combinations(cards, 3):
    candidate_sum = sum(candidate)
    if candidate_sum <= m:
        result = max(result, candidate_sum)

print(result)
