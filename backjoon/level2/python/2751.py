import sys
test_cases = int(sys.stdin.readline())

nums = list()
for _ in range(test_cases):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(*nums, sep="\n")
    
