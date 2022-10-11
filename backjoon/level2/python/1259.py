def is_palindrome(num: str):
    for idx in range(len(num)//2):
        if num[idx] != num[-(idx + 1)]:
            return False
    return True


while True:
    num = input()
    if num == "0":
        break
    print("yes" if is_palindrome(num) else "no")

