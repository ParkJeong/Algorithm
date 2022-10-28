import sys
from collections import Counter


def set_root(root, node1, node2, n):
    target_root1 = root[node1]
    target_root2 = root[node2]
    new_root = max(target_root1, target_root2)
    for node in range(n + 1):
        if root[node] in [target_root1, target_root2]:
            root[node] = new_root



n = int(sys.stdin.readline())

edge_num = int(sys.stdin.readline())

def solution1(n, edge_num):
    root = []
    for idx in range(n + 1):
        root.append(idx)
    for _ in range(edge_num):
        node1, node2 = map(int, sys.stdin.readline().split())
        set_root(root, node1, node2, n)

    root_count = Counter(root)

    print(root_count[root[1]] - 1)


# solution1(n, edge_num)


def dfs(graph, visited, n):
    visited[n] = True
    for node in graph[n]:
        if not visited[node]:
            dfs(graph, visited, node)


def solution2(n, edge_num):
    sys.setrecursionlimit(10 ** 6)
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(edge_num):
        node1, node2 = map(int, sys.stdin.readline().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    dfs(graph, visited, 1)

    print(visited.count(True) - 1)


solution2(n, edge_num)



