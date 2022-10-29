# 8시 35분
# 1_000_000
# I n 정수 삽입 동일한 정수 삽입 가능
# D 1 최댓값 삭제
# D -1 최솟값 삭제
# 동일한 최댓값, 최솟값이 2개 이상인 경우 1번의 삭제 연산으로는 1개만 삭제된다.
# 큐가 비어있는 경우 D 연산은 무시한다.
#
# 모든 연산 처리 후 큐에 남아있는 최댓값과 최솟값 출력
# 최댓값과 최솟값은 공백으로 구분해서 출력
#
# 큐가 비어있다면 EMPTY를 출력
# 1
# 7
# I 16
# I -5643
# D -1
# D 1
# D 1
# I 123
# D -1

import sys
import heapq


def solution():
    operation_num = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    exist = [False] * operation_num
    for idx in range(operation_num):
        operation, num = sys.stdin.readline().rstrip().split()
        num = int(num)
        if operation == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            exist[idx] = True
        elif operation == "D" and num == 1 and len(max_heap) > 0:
            while len(max_heap) > 0 and not exist[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if len(max_heap) > 0:
                now_num, now_idx = heapq.heappop(max_heap)
                exist[now_idx] = False
        elif operation == "D" and num == -1 and len(min_heap) > 0:
            while len(min_heap) > 0 and not exist[min_heap[0][1]]:
                heapq.heappop(min_heap)

            if len(min_heap) > 0:
                now_num, now_idx = heapq.heappop(min_heap)
                exist[now_idx] = False

    while len(max_heap) > 0 and not exist[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while len(min_heap) > 0 and not exist[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if len(min_heap) > 0:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")


test_case_num = int(sys.stdin.readline())

for _ in range(test_case_num):
    solution()
