def solution(s):
    answer = ''

    arr = list(map(int, s.split()))
    min_value = min(arr)
    max_value = max(arr)
    answer = f"{min_value} {max_value}"
    return answer


ans = solution("1 2 3 4")

print(ans)