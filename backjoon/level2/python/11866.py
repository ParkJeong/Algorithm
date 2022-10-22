import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

circle = list()
for idx in range(n):
    circle.append(idx + 1)

target_idx = 0
result_circle = list()
while (length := len(circle)) > 1:
    if target_idx + k - 1 >= length:
        n = 1
        while True:
            if target_idx + k <= length * (n + 1):
                break
            n += 1
        if target_idx + k - length * n == 0:
            target_idx = length - 1
        else:
            target_idx = target_idx + k - length * n - 1
    else:
        target_idx += k - 1
    temp = circle
    circle = circle[:target_idx]
    circle.extend(temp[target_idx + 1:])
    result_circle.append(temp[target_idx])

result_circle.append(circle[0])
print("<", end="")
result = ""
for element in result_circle:
    result += str(element) + ", "
print(result[:-2], end="")
print(">")


## 다른 사람 풀이
N, K=map(int,input().split())

n, r, l = 0 , [], list(range(1,N+1))

while len(l) > 0:
    temp = l.pop(n:=(n+K-1)%len(l))
    r.append(temp)
print(f"<{', '.join(map(str,r))}>")


# 4 3
# 3 2 4 1
# 
# 4 4
# 4 1 3 2
# 
# 4 5
# 1 3 4 2
# 4 6
# 2 4 3 1
# 4 7
# 
# 4 8
# 
# 4 9
# 
# 4 10
