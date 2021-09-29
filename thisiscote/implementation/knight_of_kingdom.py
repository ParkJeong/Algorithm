loc = input()

# 답안
input_data = loc
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
  (-2, -1),
  (-1, -2),
  (1, -2),
  (2, -1),
  (2, 1),
  (1, 2),
  (-1, 2),
  (-2, 1),
  ]

result = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1
print(result)

# 내 답

cols = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5,
  'f': 6,
  'g': 7,
  'h': 8,
  }

row, col = int(loc[1]), cols[loc[0]]
print(row, col)

dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

count = 0

for now in range(len(dx)):
  nx = row + dx[now]
  ny = col + dy[now]
  
  if (nx >= 1 and nx <= 8) and (ny >= 1 and ny <= 8):
    count += 1

print(count)

