# 2트
# 다양한 수로 이루어진 배열이있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없다.
# 인덱스가 다르면 다른 수이다.

import sys

n, m, k = sys.stdin.readline().rstrip().split()
nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort()

# 10 3
# 3 1 3 1 3

first = nums[-1]
second = nums[-2]

count = (m // (k + 1)) * k
count += m % (k + 1)

answer = count * first
answer += (m - count) * second






# 큰 수의 법칙
# 출처: 이것이 코딩 테스트다 p92
# 출처: 2019 국가 교육기관 코딩 테스트 

n, m, k = map(int, input().split())
num = list()
sum = 0

num = list(map(int, input().split()))

num.sort(reverse=True)

## 쉬운 방법

index = 0
count = 0
while count < m:
  loop = 0
  while count < m and loop < k:
    sum += num[0]
    count += 1
    loop += 1
  sum += num[1]
  count += 1

# 좀 더 제대로 푸는 방법

unit = num[0] * k + num[1]
sum = unit * (m // (k + 1))

for _ in range(m % (k + 1)):
    sum += num[0]
print(sum)
