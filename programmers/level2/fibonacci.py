# 피보나치 수 구현
# 2이상의 n이 입력
# n번째 피보나치 수를 1234567로 나눈 나머지를 리턴


import sys

FIBONACCI = dict()
FIBONACCI[0] = 0
FIBONACCI[1] = 1
FIBONACCI[2] = 1
FIBONACCI[3] = 2


def get_fibonacci(n):
    if n in FIBONACCI.keys():
        return FIBONACCI[n]
    else:
        FIBONACCI[n] = get_fibonacci(n - 1) + get_fibonacci(n - 2)
        return FIBONACCI[n]


def solution(n):
    sys.setrecursionlimit(10 ** 6)
    answer = get_fibonacci(n)

    return answer % 1234567

# print(solution(3))
print(solution(5))
print(solution(1000))
