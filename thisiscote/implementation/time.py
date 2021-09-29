target = int(input())

# 답안

h = target

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1


# 내 풀이
# python에서 숫자를 보기 좋게 하기 위해 _를 쓸 수 있다.

target = target + 1
result = 0

for hour in range(target):
  if hour // 10 == 3:
    result += 3600
    continue
  elif hour % 10 == 3:
    result += 3600
    continue
  for min in range(60):
    if min // 10 == 3:
      result += 60
      continue
    elif min % 10 == 3:
      result += 60
      continue
    for sec in range(60):
      if sec // 10 == 3:
        result += 1
      elif sec % 10 == 3:
        result += 1

print(result) 


