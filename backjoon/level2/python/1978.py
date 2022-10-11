import math
prime_nums = dict()
prime_nums[2] = True
prime_nums[3] = True


def is_prime_num(target_num: int):
    if target_num == 1:
        return False

    start_num = sorted(prime_nums)[-1]
    for num in range(start_num, int(math.sqrt(target_num)) + 1, 2):
        for prime_num in prime_nums.keys():
            if num % prime_num == 0:
                break
        else:
            prime_nums[num] = True

    if target_num in prime_nums.keys():
        return True
    for prime_num in prime_nums.keys():
        if target_num % prime_num == 0:
            return False
    return True


test_cases = int(input())

count = 0
nums = list(map(int, input().split()))
for idx in range(test_cases):
    count += 1 if is_prime_num(nums[idx]) else 0

print(count)

