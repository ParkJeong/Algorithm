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
