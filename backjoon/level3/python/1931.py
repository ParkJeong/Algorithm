import sys

n = int(sys.stdin.readline())

time_table = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append((start, end))

time_table.sort(key=lambda x: (x[1], x[0]))
prev_end_time = 0
count = 0
for start_time, end_time in time_table:
    if prev_end_time <= start_time:
        count += 1
        prev_end_time = end_time

print(count)
