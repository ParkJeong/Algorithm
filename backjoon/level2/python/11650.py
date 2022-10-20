import sys

test_case_num = int(sys.stdin.readline())

points = []
for _ in range(test_case_num):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    points.append((x, y))

# points.sort(key=lambda pos: pos[1])
points.sort(key=lambda pos: (pos[0], pos[1]))

for point in points:
    print(*point)
