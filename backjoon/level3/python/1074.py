import sys


# n 3
# r
#
# n 2짜리인 4분면 4개
# 2^4 * 0, 1, 2

# n 2
# n 1짜리인 4분면 4개
# 2^2 * 0, 1, 2
# n 1
# n 0짜리인 4분면 4개
# 2^0 * (0, 1, 2)

def divide_and_conquer(n, r, c):
    ans = 0
    while n != 0:
        n -= 1
        # 1사분면
        if r < 2 ** n and c < 2 ** n:
            ans += (2 ** (2 * n)) * 0
        # 2사분면
        elif r < 2 ** n and c >= 2 ** n:
            ans += (2 ** (2 * n)) * 1
            c -= 2 ** n
        # 3사분면
        elif r >= 2 ** n and c < 2 ** n:
            ans += (2 ** (2 * n)) * 2
            r -= 2 ** n
        # 4사분면면
        else:
            ans += (2 ** (2 * n)) * 3
            r -= 2 ** n
            c -= 2 ** n
    return ans

def recur(n, r, c):
    if n == 0:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * recur(n - 1, r//2, c//2)



n, r, c = map(int, sys.stdin.readline().rstrip().split())
# result = divide_and_conquer(n, r, c)
result = recur(n, r, c)

print(result)



# n = 3
# 4분면 각 2^4씩 증가
#
# n = 2
# 4분면 각 2^2씩 증가
#
# n = 1
# 4분면 각 2^0씩 증가
#




def divide_and_conquer2(n, r, c):
    ans = 0
    while n > 0:
        n -= 1
        if r < 2**n and c < 2**n:
            ans += 0
        elif r < 2**n and c >= 2**n:
            ans += 2**(n*2)
            c -= 2**n
        elif r >= 2**n and c < 2**n:
            ans += 2**(n*2) * 2
            r -= 2**n
        else:
            ans += 2**(n*2) * 3
            r -= 2**n
            c -= 2**n
    return ans

import sys

N, r, c  = map(int, sys.stdin.readline().rstrip().split())

result = divide_and_conquer2(N, r, c)
print(result)


### 미친놈 풀이
n, r, c = map(int, sys.stdin.readline().rstrip().split())
print(int(f"{c:b}", 4) + 2 * int(f"{r:b}", 4))
