# 2xN명의 사원들은 N명씩 두 팀으로 나눠 숫자게임
# A팀 B팀
# 1. 먼저 모든 사원이 무작위로 자연수를 하나씩 받음
# 2. 각 사원은 딱 한 번씩 경기를 함
# 3. 각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개
# 그때 숫자가 큰 쪽이 승리 -> 승리한 팀이 승점 1점 얻음
# 숫자가 같다면 누구도 승점을 얻지 못한다.
# 1 <= A, B <= 100_000
# 각 원소는 1 <= 1_000_000_000

# 투 포인터 문제
# 1. A, B 정렬
# 2. A에 포인터 하나 B에 포인터 하나
# 3. A보다 B가 같거나 작으면 B의 포인터 +1(먼저 체크, 포인터가 B배열 밖으로 안 벗어나게 벗어나면 끝)
#   A보다 B가 크면 A와 B의 포인터 + 1((먼저 체크, 포인터가 A,B배열 밖으로 안 벗어나게 벗어나면 끝))
#   result += 1
# 4. 반복문 나오고 result 출력

def solution(A, B):
    a_idx = 0
    b_idx = 0
    answer = 0

    A.sort()
    B.sort()
    # while True:
    #     if a_idx >= len(A) or b_idx >= len(B):
    #         break
    #     elif A[a_idx] >= B[b_idx]:
    #         b_idx += 1
    #     elif A[a_idx] < B[b_idx]:
    #         a_idx += 1
    #         b_idx += 1
    #         answer += 1
    for b in B:
        a = A[a_idx]
        if a < b:
            a_idx += 1
            answer += 1
    return answer


print(solution([5,1,3,7]	,[2,2,6,8]))
print(solution([2,2,2,2]	,[1,1,1,1]))
