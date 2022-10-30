# from collections import deque


# def solution(s):
#     answer = True
#
#     target = deque(s)
#
#     count = 0
#     while len(target) > 0:
#         now = target.popleft()
#         if now == "(":
#             count += 1
#         elif now == ")":
#             count -= 1
#         if count < 0:
#             break
#     if count != 0:
#         answer = False
#     return answer


def solution(s):
    answer = True

    count = 0
    for ch in s:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
        if count < 0:
            break
    if count != 0:
        answer = False
    return answer
