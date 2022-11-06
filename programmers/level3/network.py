# 1 <= 컴퓨터의 개수 <= 200 자연수
# 컴퓨터는 0부터 n-1인 정수로 표현됨
# i와 j가 연결되어 있으면 computers[i][j] == 1로 표현
# computers[i][i]는 항상 1이다.
# 네트워크 개수를 리턴

# 예시
# 1 1 0
# 1 1 0
# 0 0 1
# -> 2

# 예시2
# 1 1 0
# 1 1 1
# 0 1 1
# 0 -> 1, 1 -> 0, 1 -> 2, 2 -> 1

# 노드별로 루트 노드를 자기 자신으로 설정
# 연결된 노드인 경우 루트 노드를 가장 작은 숫자인 노드로 변경

# 1. i와 연결된 모든 node의 값 count로 변경
# 2. i와 연결되 모든 node로 1 수행

from collections import deque


def solution2(n, computers):
    def bfs(start, count):
        queue = deque()
        for end in range(n):
            if computers[start][end] == 1:
                computers[start][end] = count
                queue.append(end)

        while queue:
            new_start = queue.popleft()
            bfs(new_start, count)
        count += 1

    count = 2
    for i in range(n):
        bfs(i, count)

def solution(n, computers):

    root_node = [idx for idx in range(n)]

    def union_root_node(old_root, new_root):
        for root_idx in range(len(root_node)):
            if root_node[root_idx] == old_root:
                root_node[root_idx] = new_root

    def set_root_node(node1, node2):
        if root_node[node1] > root_node[node2]:
            union_root_node(root_node[node1], root_node[node2])
        else:
            union_root_node(root_node[node2], root_node[node1])

    for node1 in range(n):
        for node2 in range(n - 1):
            if node1 == node2:
                continue
            if computers[node1][node2] == 1 and root_node[node1] != root_node[node2]:
                set_root_node(node1, node2)
    answer = len(set(root_node))

    return answer

print(solution(3, [[1,0,0],[0,1,0],[0,0,1]]))
print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))
print(solution(3, [[1,1,1],[1,1,0],[1,0,1]]))
print(solution(3, [[1,1,1],[1,1,1],[1,1,1]]))

