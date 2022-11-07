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
    count = length - plan.count(0)
    visited = [False for _ in range(length)]

    # 초깃값
    count -= 0 if plan[0] == 0 else 1
    answer = plan[0]
    visited[0] = True

    # 매번 가장 가까운 곳으로 이동
    # 왼쪽으로 가장 가까운 곳 a, 먼 곳 b
    # 오른쪽으로 가장 가까운 곳 c, 먼 곳 d
    # min(min(b, d) * 2 + max(b, d), length - d) + 알파벳 변환
    #
    #
    # 완전탐색으로도 풀어보기
    answer += sum(plan)
    return answer


solution("JEROEN")