import sys

result = dict()
result[0] = (1, 0)
result[1] = (0, 1)


def solution(num):
    if num in result.keys():
        return result[num]

    left_num = solution(num - 1)
    right_num = solution(num - 2)
    result[num] = (left_num[0] + right_num[0], left_num[1] + right_num[1])
    return result[num]


test_case_num = int(sys.stdin.readline())

for _ in range(test_case_num):
    test_case = int(sys.stdin.readline())
    print(*solution(test_case))
