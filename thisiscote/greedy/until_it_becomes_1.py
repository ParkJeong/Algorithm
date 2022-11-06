# 2트
# 어떤 수 N이 1이 될 때까지  두 과정 중 하나를 반복해서 수행
# N에서 1을 뺌
# N을 k로 나눔

import sys
import time

start_time = time.time()
########################
n, k = map(int, sys.stdin.readline().split())

count = 0
while n > 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1

print(count)
########################
end_time = time.time()
print(f"time: {end_time - start_time}")

n, k = map(int, input().split())

# 답안
# k가 충분히 클 때 효율적이다.
result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)


# 내 풀이
count = 0
while n > 1:
  if n % k == 0:
    n //= k
  else:
    n -= 1
  count += 1

print(count)
