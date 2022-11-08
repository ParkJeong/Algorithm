# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수를 구하려곻 한다.
# 1924에서 숫자 2개를 제거할 때 만들 수 있는 가장 큰수 94
# 문자열 형식 숫자 2 <= number <= 1_000_000
# 제거할 수의 개수 1 <= k < number 의 자릿수  자연수
# 풀이

# 가장 큰 수 다음으로 넘어간다.

from collections import deque

def solution(number, k):
    answer = ''
    # stack을 이용해서 구현해보기


    return number


# print(solution("1924", 2))

# print(solution("1231234", 3))

print(solution("4177252841", 4))
print(solution("1111", 4))
