from collections import deque


def is_vps(line):
    string = deque(line)

    count_left_parenthesis = 0
    while len(string) > 0:
        now_ch = string.popleft()
        if now_ch == "(":
            count_left_parenthesis += 1
        elif now_ch == ")":
            count_left_parenthesis -= 1

        if count_left_parenthesis < 0:
            break

    return count_left_parenthesis == 0


def solution(test_cases):
    for test_case in test_cases:
        if is_vps(test_case):
            print("YES")
        else:
            print("NO")


test_case_num = int(input())

test_cases = []
for _ in range(test_case_num):
    test_cases.append(input())
solution(test_cases)