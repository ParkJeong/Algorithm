
def solution(s):
    is_first = True
    jaden_case = ""
    for ch in s:
        if is_first and ch != " ":
            jaden_case += ch.upper()
            is_first = False
            continue
        jaden_case += ch.lower()
        if ch == " ":
            is_first = True
    return jaden_case



ans = "3people   unFollowed me".capitalize()
print(ans)
ans = solution("3people   unFollowed me")
print(ans)
ans = solution("for the last week")
print(ans)
ans = solution("1 t L 1A3 dA1A 1a4")
print(ans)
