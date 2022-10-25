import sys

poketmon_num, test_case_num = map(int, sys.stdin.readline().rstrip().split())

poketdex_by_idx = dict()
poketdex_by_name = dict()
for idx in range(1, poketmon_num + 1):
    poketmon = sys.stdin.readline().rstrip()
    poketdex_by_idx[idx] = poketmon
    poketdex_by_name[poketmon] = idx

for _ in range(test_case_num):
    test_case = sys.stdin.readline().rstrip()
    if test_case.isdigit():
        result = poketdex_by_idx[int(test_case)]
    else:
        result = poketdex_by_name[test_case]
    print(result)