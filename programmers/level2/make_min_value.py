# 길이가 같은 두 배열
# 배열은 모두 자연수로 이루어짐
# 각각의 배열에서 하나씩 뽑아서 두 수를 곱함
# 배열의 길이만큼 반복
# 두 수를 곱한 값을 누적해서 더한다.
# 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표
# 중복해서 뽑을 수는 없다.


def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    answer = 0
    for idx in range(len(A)):
        answer += A[idx] * B[idx]
    return answer

