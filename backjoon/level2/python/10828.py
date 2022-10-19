import sys
from collections import deque

cmd_case_num = int(sys.stdin.readline())

stack = deque()
for _ in range(cmd_case_num):
    cmd_list = sys.stdin.readline().rstrip().split()
    if len(cmd_list) == 2:
        cmd = cmd_list[0]
        element = cmd_list[1]
    else:
        cmd = cmd_list[0]

    if cmd == "push":
        stack.append(element)
        continue
    elif cmd == "pop":
        result = -1 if len(stack) == 0 else stack.pop()
    elif cmd == "size":
        result = len(stack)
    elif cmd == "empty":
        result = 1 if len(stack) == 0 else 0
    elif cmd == "top":
        result = -1 if len(stack) == 0 else stack[-1]
    print(result)


