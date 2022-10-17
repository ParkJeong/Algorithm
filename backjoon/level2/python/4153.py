import math

def is_over(side1, side2, side3):
    return side1 == 0 or side2 == 0 or side3 == 0


def get_each_side(side1, side2, side3):
    hypotenuse = max(side1, side2, side3)
    if side1 == hypotenuse:
        height = max(side2, side3)
        base = min(side2, side3)
    elif side2 == hypotenuse:
        height = max(side1, side3)
        base = min(side1, side3)
    else:
        height = max(side1, side2)
        base = min(side1, side2)
    return hypotenuse, height, base


# pow(x, y) 는 x의 y 제곱이다.
def is_right_triangle(side1, side2, side3):
    hypotenuse, height, base = get_each_side(side1, side2, side3)

    return math.pow(hypotenuse, 2) == math.pow(height, 2) + math.pow(base, 2)


while True:
    # 입력받을 때부터
    # 정렬하면 됐다...
    # 그러면 훨씬 쉬웠겠다....
    # 다시 풀기
    side1, side2, side3 = map(int, input().split())

    if is_over(side1, side2, side3):
        break

    if is_right_triangle(side1, side2, side3):
        print("right")
    else:
        print("wrong")

