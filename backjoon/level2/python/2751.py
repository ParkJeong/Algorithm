test_cases = int(input())

nums = list()
for _ in range(test_cases):
    nums.append(int(input()))

for element in sorted(nums):
    print(element)
    
    n