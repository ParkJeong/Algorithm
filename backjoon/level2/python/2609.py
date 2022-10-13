# greatest common divisor
# 디바^이져
def get_gcd(num1, num2):
    if num1 > num2:
        a, b = num1, num2
    else:
        a, b = num2, num1

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def get_gcd_by_recursive(num1, num2):
    if num1 > num2:
        return __get_gcd_by_recursive(num1, num2)
    else:
        return __get_gcd_by_recursive(num2, num1)


def __get_gcd_by_recursive(num1, num2):
    if num2 == 0:
        return num1
    return get_gcd_by_recursive(num2, num1 % num2)


# least common multiple
# lowest common multiple
# 최소 공배수는 두 수 n, m을 곱하고 n,m의 최대 공약수로 나눈 값과 같다.
def get_lcm(num1, num2):
    gcd = get_gcd(num1, num2)
    return int(num1 * num2 / gcd)


num1, num2 = map(int, input().split())

print(get_gcd_by_recursive(num1, num2))
print(get_lcm(num1, num2))
