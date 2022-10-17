test_case_num = int(input())


test_cases = list()
for idx in range(test_case_num):
    age, name = input().split()
    test_cases.append((idx, age, name))


test_cases.sort(key=lambda x: x[1])
print("="*100)
for test_case in test_cases:
    print(test_case[1], test_case[2])

test_cases.sort(key=lambda x: x[2])
print("=" * 100)
for test_case in test_cases:
    print(test_case[1], test_case[2])

