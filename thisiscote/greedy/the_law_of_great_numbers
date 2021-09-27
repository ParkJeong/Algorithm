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
