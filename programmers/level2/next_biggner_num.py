# n의 다음 큰 숫자는 n보다 큰 자연수
# n의 다음 큰 숫자와 n은 2진수로 변환햇을 때 1의 갯수가 같다.
# n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 이다.
# 78(1001110)의 다음 큰 숫자는 83(1010011)

def solution(n):
    answer = n

    count_one = bin(n)[2:].count("1")
    while True:
        answer += 1
        candidate = bin(answer)
        candi_count_one = candidate[2:].count("1")
        if candi_count_one == count_one:
            break

    return answer
