import sys
from collections import deque

cmd_case_num = int(sys.stdin.readline())

_deque = deque()
for _ in range(cmd_case_num):
    cmd_list = sys.stdin.readline().rstrip().split()

    if len(cmd_list) == 2:
        cmd, element = cmd_list
    else:
        cmd = cmd_list[0]

    if cmd == "push_front":
        _deque.appendleft(element)
        continue
    if cmd == "push_back":
        _deque.append(element)
        continue
    elif cmd == "pop_front":
        result = -1 if len(_deque) == 0 else _deque.popleft()
    elif cmd == "pop_back":
        result = -1 if len(_deque) == 0 else _deque.pop()
    elif cmd == "size":
        result = len(_deque)
    elif cmd == "empty":
        result = 1 if len(_deque) == 0 else 0
    elif cmd == "front":
        result = -1 if len(_deque) == 0 else _deque[0]
    elif cmd == "back":
        result = -1 if len(_deque) == 0 else _deque[-1]

    print(result)