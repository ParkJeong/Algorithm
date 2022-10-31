# 주어진 항공권 모두 사용
# 항상 ICN에서 출발
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어짐
# 방문하는 공항 경로를 배열에 담아 return
# 모든 공항은 알파벳 대문자 3글자
# 주어진 공항 수는 3 <= <=10_000
# tickets의 각 행 a,b는 a공항에서 b로 가는 항공권이 있다는 의미
# 주어진 항공권 모두 사용
# 가능한 경로가 2개 이상일 겨웅 알파벳 순서가 앞서는 경로 우선
# 모든 도시를 방문할 수 없는 경우 X
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# -> ["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# 100_000_000
# 요소 1이 ICN인 것을 찾고
# dict에 출발지를 key(문자열) 도착지 리스트를 value로 하는 route 저장 log(n)
# icn꺼냄 q에 담음

from collections import deque


def exist_next_dest(route, now):
    return now in route.keys()


def solution(tickets):
    answer = []

    route = dict()

    for ticket in tickets:
        if ticket[0] not in route:
            route[ticket[0]] = list()
        route[ticket[0]].append(ticket[1])

    for key in route:
        route[key].sort()
        route[key] = deque(route[key])

    start = "ICN"
    answer.append(start)
    while len(route) > 0:
        dest = route[start].popleft()
        if len(route) == 1 or exist_next_dest(route, dest):
            answer.append(dest)
        else:
            route[start].append(dest)
            continue
        if len(route[start]) == 0:
            del route[start]
            if len(route) == 0:
                break
        start = dest

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))

print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
