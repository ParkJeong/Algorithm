from heapq import heappush, heappop
import sys
test_case_num = int(sys.stdin.readline())
heap = []

for _ in range(test_case_num):
    test = int(sys.stdin.readline().rstrip())
    if test == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, test)

# n, *test_cases = open(0).read().split()
#
# for test in test_cases:
#     if test == "0":
#         if len(heap) == 0:
#             print(0)
#         else:
#             print(heappop(heap))
#     else:
#         heappush(heap, int(test))