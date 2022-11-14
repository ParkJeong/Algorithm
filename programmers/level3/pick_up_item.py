# 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동한다.
# 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현
# 캐릭터는 다각형의 둘레를 따라 이동
# 서로 다른 두 직사각형의 x축 좌표나 y축 좌표가 같은 경우는 없다.
# -> 꼭짓점이 겹치거나, 변이 겹치는 경우는 없다.
# 두 개 지형으로 나뉘는 것도 없다. 총 1개의 다각형만 생김
# 한 직사각형이 다른 직사각형에 완전히 포함되는 경우도 없다.
# 1 <= rectangle 의 세로(행) 길이 <=4
# rectangle 의 원소 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
# 1 <= 모든 좌표 값 <= 50 자연수
# 조건에 맞는 rectangle 만 입력으로 주어짐
# 캐릭터는 다각형 테두리 위의 한 점으로 주어진다.
# 1 <= characterX, characterY <= 50 인 자연수
# 아이템은 다각형 테두리 위의 한 점으로 주어진다.
# 1 <= itemX, itemY <= 50 인 자연수

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    BOARD_WIDTH = 50
    BOARD_HEIGHT = 50


    # 전체 크기 50 x 50 = 2500 -> 4kb * 2.5 = 10kb 충분
    # 전체 맵 만들기
    board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

    # 직사각형을 받아서 다각형의 둘레를 맵에 표시
    for temp_rectangle in rectangle:
        start_x = temp_rectangle[0]
        start_y = temp_rectangle[1]
        end_x = temp_rectangle[2]
        end_y = temp_rectangle[3]

        for temp_x in range(start_x, end_x + 1):
            for temp_y in range(start_y, end_y + 1):
                board[temp_y][temp_x] = 1

    # #  직사각형을 모두 맵에 표시
    # #  각 행별로 가장 왼쪽과 가장 오른쪽 좌표만 놔두고 모두 삭제
    is_first_row = True
    last_row = (-1, -1, -1)
    for temp_y in range(BOARD_HEIGHT):
        is_first = True
        first_x = -1
        last_x = -1

        # 각 행별로 가장 왼쪽과 가장 오른쪽 기억
        for temp_x in range(BOARD_WIDTH):
            if board[temp_y][temp_x] == 1:
                if is_first:
                    first_x = temp_x
                    is_first = False
                last_x = temp_x

        # 수정해야함 22/11/14
        # 둘레를 살려야함...
        # 각 행별로 가장 왼쪽과 가장 오른쪽 사이에 모든 곳 삭제
        if not is_first:
            if is_first_row:
                is_first_row = False
            else:
                last_row = (temp_y, first_x, last_x)
                for remove_x in range(first_x + 1, last_x):
                    board[temp_y][remove_x] = 0
    # 마지막 줄 살리기
    for temp_x in range(last_row[1], last_row[2] + 1):
        board[last_row[0]][temp_x] = 1

    # 캐릭터의 위치에서 맵의 아이템 까지 최단거리 찾기 BFS
    board[characterY][characterX] = 0
    queue = deque()
    queue.append((characterX, characterY))

    DIRECTION_X = [1, 0, -1, 0]
    DIRECTION_Y = [0, 1, -1, 0]
    while True:
        x, y = queue.popleft()
        if x == itemX and y == itemY:
            return board[itemY][itemX]

        for move_x, move_y in zip(DIRECTION_X, DIRECTION_Y):
            next_x = x + move_x
            next_y = y + move_y
            if 0 <= next_x < 50 and 0 <= next_y < 50 and board[next_y][next_x] == 1:
                board[next_y][next_x] = board[y][x] + 1
                queue.append((next_x, next_y))


# print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))

