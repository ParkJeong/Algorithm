import sys
import time

start_time = time.time()
##########################
# n < 1_000_000
# 0 0 0
# 0 0 0 0 0 0  0번 바뀜 > 0

# 0 0 0 0 0 1  1번 바뀜 > 1
# 0 1 0 0 0 0  2번 바뀜 > 1

# 0 1 0 0 0 1  3번 바뀜 > 2
# 0 1 0 1 1 0  4번 바뀜 > 2

# 0 1 0 1 0 1  5번 바뀜 > 3
# 0 1 0 1 0 1 0 6번 바뀜 > 3
import sys
n = sys.stdin.readline().rstrip()
changed = 0
before = n[0]
for ch in n:
    if before != ch:
        changed += 1
    before = ch

count = 0
count += changed // 2 + changed % 2
print(count)


def solution(n):
    changed = 0
    before = n[0]
    for ch in n:
        if before != ch:
            changed += 1
        before = ch

    count = 0
    count += changed // 2 + changed % 2
    print(count)

solution("0001100") # 1

solution("11111") # 0
solution("00000001") # 1
solution("11001100110011000001") # 4
solution("11101101") # 2
solution("11001100001") # 2
solution("000000") # 0
solution("000001") # 1
solution("010000") # 1
solution("010001") # 2
solution("010100") # 2

###########################
end_time = time.time()
# print(f"시간: {end_time - start_time}")
