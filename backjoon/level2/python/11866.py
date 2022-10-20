import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

circle = list()
for idx in range(n):
    circle.append(idx)

target = 0
result = list()
while (length := len(circle)) > 1:
    if target + k >= length:
        n = 1
        while target + k >= length * n:
            n += 1
        target = target + k - length * n
    else:
        target += k
    temp = circle
    circle = circle[:target]
    circle.extend(temp[target + 1:])
    result.append(target)

print("<", end="")
print(*result, end="")
print(">")
