from typing import List


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


def get_repaint_num_with_one_letter(target_board: List[str], cell_value: List[str], start: Point):
    count = 0
    s_row = start.x
    s_col = start.y
    for row in range(s_row, s_row + 8):
        row_idx = row - s_row
        now = cell_value[row_idx % 2]
        for col in range(s_col, s_col + 8):
            col_idx = col - s_col
            cell = target_board[row][col]
            if cell != now:
                count += 1
            now = cell_value[(row_idx + col_idx + 1) % 2]
    return count


def get_repaint_num_with_both(target_board: List[str], start: Point):
    cell_value = ["B", "W"]
    count_with_x = get_repaint_num_with_one_letter(target_board, cell_value, start)
    cell_value = ["W", "B"]
    count_with_y = get_repaint_num_with_one_letter(target_board, cell_value, start)
    return min(count_with_x, count_with_y)


row, col = map(int, input().split())

board = list()
for _ in range(row):
    board.append(input())

result = 987654321
for start_col in range(col - 8 + 1):
    for start_row in range(row - 8 + 1):
        start = Point(start_row, start_col)
        now_result = get_repaint_num_with_both(board, start)
        result = min(result, now_result)
print(result)
