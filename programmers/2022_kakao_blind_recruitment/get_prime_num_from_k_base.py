"""
###새로 배운 내용
divmod(a, b)는 a,b가 큰 수일 때 a//b, a%b보다 빠르다.
수의 크기가 작을 때는 a//b, a%b가 더 빠르다.

quotient:   몫
rest:       나머지

k진수 -> 10진수 변환
int(n, k)

10진수 -> k진수 변환
직접 구현

n진수 -> m진수 변환
n진수 -> 10진수 -> m진수 변환

import math
math.sqrt(n)    # n == 4 -> 4

int(n) + 1      # n == 4 -> 5

###아이디어
진법 변환
소수 판별
"""
import string
import math
tmp = string.digits + string.ascii_lowercase


def convert_to_k_base(n, base):
    quotient, rest = divmod(n, base)
    if quotient == 0:
        return tmp[rest]
    else:
        return convert_to_k_base(quotient, base) + tmp[rest]


def is_prime_num(n):
    n = int(n)
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    n_to_k_base = convert_to_k_base(n, k)

    n_to_k_base_split_by_zero = n_to_k_base.split("0")
    for num in n_to_k_base_split_by_zero:
        if num != "":
            if is_prime_num(num):
                answer += 1

    return answer

