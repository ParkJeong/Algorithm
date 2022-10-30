# x의 모든 0을 제거
# x의 길이가 c인 경우, x를 c를 2진법으로 표현한 문자열로 바꾼다.
# x = 0111010 -> 1111 -> 100 -> 1
# 110010101001 -> 111111 -> 110 -> 11 -> 10 -> 1

def remove_zero(s):
    result = ""
    removed_zero_num = 0
    for ch in s:
        if ch == "1":
            result += ch
        else:
            removed_zero_num += 1
    return result, removed_zero_num


def solution(s):
    answer = [0, 0]

    while s != "1":
        s, removed_zero_num = remove_zero(s)
        length = len(s)
        s = bin(length)[2:]

        answer[0] += 1
        answer[1] += removed_zero_num

    return answer
