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
