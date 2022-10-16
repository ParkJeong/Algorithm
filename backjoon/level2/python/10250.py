def solution(test_case):
    height, width, customer_num = test_case

    width_num = (customer_num - 1) // height + 1
    height_num = customer_num % height

    if width_num <= 9:
        width_num = str(0) + str(width_num)
    else:
        width_num = str(width_num)

    if height_num == 0:
        height_num = str(height)
    else:
        height_num = str(height_num)

    room_num = height_num + width_num
    return room_num


test_case_num = int(input())
test_cases = []
for _ in range(test_case_num):
    height, width, customer_num = list(map(int, input().split()))
    test_cases.append((height, width, customer_num))

for test_case in test_cases:
    print(solution(test_case))
