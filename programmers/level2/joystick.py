# 조이스틱으로 알파벳 완성
# 알파벳은 링버퍼
# 위: 다음 알파벳
# 아래: 이전 알파벳
# 오른쪽: 커서를 오른쪽으로 이동
# 왼쪽: 커서를 왼쪽으로 이동

# 맨 처음엔 A로만 이루어져있다.
# 3글자라면 AAA, 4글자라면 AAAA
# 각 글자마다 변해야하는 수 저장
# ord("") - ord("A")

# AABAAAB
# 매번 가장 가까운 곳으로 이동해서 변경
# 왜 정당한가?

# 매번 가장 가까운 곳을 선택한다면 가장 거리가 짧다
# 가장 거리가 먼곳은 매번 가장 먼곳을 선택한 것이다.
# ABABAAAAAB
# 1 2 6 OR 1 2 2


def solution(name):
    plan = []

    # 각 글자마다 변해야하는 수 저장
    for ch in name:
        plan.append(min(ord(ch) - ord("A"), ord("Z") - ord(ch) + 1))

    length = len(name)
    answer = 0
    # 매번 가장 가까운 곳으로 이동
    # 왼쪽으로 가장 가까운 곳 a, 먼 곳 b
    # 오른쪽으로 가장 가까운 곳 c, 먼 곳 d
    # min(min(b, d) * 2 + max(b, d), length - d) + 알파벳 변환

    def find_the_nearest_position():
        now = 0
        right = 0
        left = 0

        for right_idx in range(length):
            if plan[now] != 0:
                right = right_idx
                break
        for left_idx in range(0, -length, -1):
            if plan[now] != 0:
                left = left_idx
                break
        return left, right

    def find_the_furthest_position():
        now = 0
        right = 0
        left = 0

        for right_idx in range(-1, -(length + 1), -1):
            if plan[now] != 0:
                right = right_idx
                break
        for left_idx in range(1, length):
            if plan[now] != 0:
                left = left_idx
                break
        return left, right

    furthest_left_pos, furthest_right_pos = find_the_furthest_position()
    furthest_right_pos = furthest_right_pos if furthest_right_pos >= 0 else length + furthest_right_pos

    distance_from_furthest_left_pos = furthest_left_pos
    distance_from_furthest_right_pos = furthest_right_pos
    # 매번 가장 가까운 곳으로 이동
    # 왼쪽으로 가장 가까운 곳 a, 먼 곳 b
    # 오른쪽으로 가장 가까운 곳 c, 먼 곳 d
    # min(min(b, d) * 2 + max(b, d), length - d) + 알파벳 변환
    # 왼쪽으로 가장 먼 것과 오른쪽으로 가장 먼 것 사이에 있는 경우 처리가 안됨 -> JEROEN의 경우
    move = min(
        min(
            distance_from_furthest_left_pos,
            distance_from_furthest_right_pos
        ) * 2
        + max(distance_from_furthest_left_pos, distance_from_furthest_right_pos),
        min(
            length - distance_from_furthest_left_pos,
            length - distance_from_furthest_right_pos
        )
    )


    #
    # 완전탐색으로도 풀어보기
    answer += sum(plan)
    answer += move
    return answer


# A -> J : 9
# A -> N : 13
# A -> E : 4
# A -> R : 17  -> 9
# ZYXWVUTSRQPONML
# A -> O : 14 -> 12
# 이동 2
# print(solution("JAN"))
# 9 + 4 + 9 + 12 + 4 + 13
# 51 + 5(이동)
print(solution("JEROEN"))