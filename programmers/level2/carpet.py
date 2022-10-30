# 갈색 격자 수 8 <= <=5_000
# 노란색 격자 수 1<= <=2_000_000
# 카펫의 가로 길이는 세로 길이와 같거나 세로 길이보다 길다.
# 중앙에는 노란색, 테두리 1줄은 갈색
import math


def solution(brown, yellow):
    for width in range(1, 2500):
        for height in range(1, math.ceil(math.sqrt(2_000_000))):
            if width * 2 + height * 2 - 4 == brown and (width - 2) * (height - 2) == yellow and width >= height:
                return [width, height]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
