# 한자리 숫자가 적힌 종이 조각이 흩어져 있다.
# 흩어진 종이 조각을 붙여 소수를 몇개 만들 수 있는지 알아보자.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졋다.
# 이 때, 종이조각으로 만들 수 있는 소수가 몇 개인지 return
# numbers는 길이가 1이상 7이하
#  number는 0~9로만 이루어짐
# 013은 0,1,3 숫자가 적힌 종이 조각이 흩어져 있다는 뜻

from itertools import permutations
import math
PRIME_NUM = dict()
PRIME_NUM[0] = False
PRIME_NUM[1] = False
PRIME_NUM[2] = True
PRIME_NUM[3] = True
PRIME_NUM[5] = True
PRIME_NUM[7] = True


def is_prime_num(num):
    if num in PRIME_NUM.keys():
        return PRIME_NUM[num]
    if num % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            PRIME_NUM[num] = False
            return PRIME_NUM[num]
    PRIME_NUM[num] = True
    return PRIME_NUM[num]


def solution(numbers):
    answer = set()

    for pick in range(1, len(numbers) + 1):
        for candidate_tuple in permutations(numbers, pick):
            candidate = "".join(candidate_tuple)
            if is_prime_num(int(candidate)):
                answer.add(int(candidate))

    return len(answer)


print(solution("17"))
print(solution("011"))