# 알파벳 소문자로 이루어진 문자열을 가지고 시작
# 1. 문자열에서 같은 알파벳이 2개 붙어있는 짝 찾기
# 2. 그 둘을 제거
# 3. 앞뒤로 이어 붙임
# 4. 이 과정을 반복
# 짝지어 제거하기를 성공적으로 수행할 수 있다면 1을 리턴 아니면 0을 리턴

# 1. 글자 확인
# 2. stack 이 비어있으면 1로 돌아감 아니면 stack의 맨 처음것과 비교
# 3. 같으면 stack pop continue 다르면 현재 요소를 stack push
# 모든 글자가 끝날때까지 진행
# 끝나고 stack이 비어있으면 1 아니면 0

from collections import deque


def solution(s):
    stack = deque()

    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
            continue
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    answer = 1 if len(stack) == 0 else 0
    return answer


# print(solution("aaaa"))     # 1
# print(solution("aaaaa"))    # 0
# print(solution("a"))        # 0
#
# print(solution(""))         # 1
# print(solution("abccba"))   # 1
# print(solution("abcacba"))  # 0
print(solution("abcda"))  # 0
