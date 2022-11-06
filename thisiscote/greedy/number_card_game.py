# 2트
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다.
# 이때 n은 행의 개수, M은 열의 개수를 의미
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 행을 선택

import sys

row, col = sys.stdin.readline().split()

cards = [[] for _ in range(col)]
for idx in range(col):
  cards[idx] += sorted(map(int, sys.stdin.readline().split()))

answer = -987654321
for idx in range(col):
  answer = max(answer, cards[idx][0])
print(answer)

n, m = map(int, input().split())

# 답안
# 바로 처리할 수 있고, 나중에 쓸 일이 없다면
# 저장하지 말고 바로 처리하자.
result = 0
for _ in range(n):
  row = list(map(int, input().split()))
  rowMin = min(row)
  result = max(result, rowMin)

print(result)


# 나의 풀이
matrix = [[0] * m for _ in range(n)]
for rowIdx in range(n):
  idx = 0
  for element in map(int, input().split()):
    matrix[rowIdx][idx] = element
    idx += 1

maxValue = -1
for rowList in matrix:
  rowMin = min(rowList)
  maxValue = maxValue if rowMin < maxValue else rowMin

print(maxValue)
