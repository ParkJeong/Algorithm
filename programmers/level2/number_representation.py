# 자연수 n을 연속한 자연수들로 표현하는 방법이 여러개
# n이 주어졌을 때 연속된 자연수들로 n을 표현하는 방법의 수를 return
# n은 10_000이하의 자연수

def solution(n):
    answer = 0

    left = 1
    right = 1

    sum_result = 1
    while True:
        while sum_result < n:
            right += 1
            sum_result += right
        if sum_result == n:
            answer += 1
            if right < n:
                right += 1
                sum_result += right
            else:
                break
        while sum_result > n:
            sum_result -= left
            left += 1

    return answer
