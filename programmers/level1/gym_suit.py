#  학생들이ㅡ 번호는 체격순
# 바로 앞 번호의 학생이나 바로 뒷 번호의 학생에게만 빌릴 수 있다.
# 최댓값
# 2 <= 전체 학생 수 <= 30
# 1 <= 도난당한 학생 중복 x <= n
# 1 <= 여벌 중복 x<= n
# 여벌을 가져온 학생도 도난당했을 수 있다. 다른 학생에게 빌리려줄 수 없다

def solution(n, lost, reserve):
    answer = n

    lost.sort()
    reserve.sort()

    for stu in lost:
        if stu in reserve:
            reserve.remove(stu)
        elif stu - 1 in reserve:
            reserve.remove(stu - 1)
        elif stu + 1 in reserve and stu + 1 not in lost:
            reserve.remove(stu + 1)
        else:
            answer -= 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))

print(solution(3, [3], [3]))
print(solution(3, [2, 3], [2]))
print(solution(7, [2, 4, 7], [1, 3, 5]))

print(solution(7, [4, 2], [3, 5]))
print(solution(4, [1, 3], [2, 4]))
print(solution(8, [5, 6, 7], [4, 5]))

print(solution(10, [3, 4], [4, 5]))
