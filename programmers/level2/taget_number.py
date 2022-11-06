# n 개의 음이 아닌 정수가 있다.
# 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만든다.
# 11111
# -> -1 1111
# -> 1 -1 111
# -> 11 -1 11
# -> 111 -1 1
# -> 1111 -1
# 2 <= 주어는 숫자의 개수 <= 20 자연수
# 1 <= 각 숫자 <= 50 자연수
# 1 <= 타겟 넘버 <= 1000 자연수
# 2^20 = 1_000_000
#
# 현재 경로에서 다음 경로로 갈 때는 + -를 해야한다.
# 굳이 방문체크할 필요 없을 듯
# 각 단계를 표시하고 마지막 단계일 때 target 인지만 확인

result = 0


def get_target_number(numbers, target, step, candidate):
    global result
    if step == len(numbers):
        result += 1 if candidate == target else 0
        return

    next_step = step + 1
    get_target_number(numbers, target, next_step, candidate + numbers[step])
    get_target_number(numbers, target, next_step, candidate - numbers[step])


def get_target_number2(numbers, target):
    from collections import deque

    queue = deque()
    queue.append((1, numbers[0]))
    queue.append((1, -numbers[0]))

    result2 = 0
    while queue:
        now_step, candidate = queue.pop()
        if now_step == len(numbers) and candidate == target:
            result2 += 1

        if now_step < len(numbers):
            queue.append((now_step + 1, candidate + numbers[now_step]))
            queue.append((now_step + 1, candidate - numbers[now_step]))

    return result2


def solution(numbers, target):
    get_target_number(numbers, target, 0, 0)
    # result = get_target_number2(numbers, target)
    return result




from itertools import product