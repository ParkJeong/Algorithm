# 2트
import time
import sys

start_time = time.time()
#######################
n = int(sys.stdin.readline())
three_not_in_hour = (5 * 9 * 5 * 2 + 5 * 9 * 9 * 2) + (5 * 9 * 4 + 5 * 5 + 9 * 9) + (5 * 2 + 9 * 2) + 1
three_in_hour = 6 * 10 * 6 * 10

count = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            candidate = f"{h}{m}{s}"
            if "3" in candidate:
                count += 1


# 03 xx xx
# 13
# 23

# 03 xx xx
# xxx3 595
# xx3x 599
# x3xx 559
# 3xxx 959

# 33xx 59
# 3x3x 99
# 3xx3 95
# x33x 59
# x3x3 55
# xx33 59

# 333x 9
# 33x3 5
# 3x33 9
# x333 5

# 3333

#######################
end_time = time.time()


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


