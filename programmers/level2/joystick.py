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

    answer = sum(plan)
    length = len(name)
    # 매번 가장 가까운 곳으로 이동
    # 그 중 최솟값을 구한다.
    candidates = set()

    def dfs(now_position, total_move, new_plan):
        new_plan[now_position] = 0
        if total_move >= length:
            return
        if new_plan.count(0) == length:
            candidates.add(total_move)

        for next_move in [-1, 1]:
            next_position = now_position + next_move
            if next_position == -1:
                next_position = length - 1
            elif next_position == length:
                next_position = 0
            temp_plan = new_plan[:]
            dfs(next_position, total_move + 1, temp_plan)

    dfs(0, 0, plan)
    answer += min(candidates)
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
# ABAAAAAAAAABB
# print(solution("JEROEN"))
print(solution("ABAAAAAAAAABB")) # 3 + 4