import sys


def get_solid_paper(paper):
    blue_count = 0
    white_count = 0
    for row in paper:
        blue_count += row.count(1)
        white_count += row.count(0)
        if blue_count * white_count != 0:
            return 0, 0
    return (1, 0) if white_count > 0 else (0, 1)


def get_new_paper(paper, start_point, end_point):
    new_paper = []
    for row in paper[start_point[1]:end_point[1]]:
        new_paper.append(row[start_point[0]:end_point[0]])
    return new_paper


def count_paper(paper, length):
    white_count, blue_count = get_solid_paper(paper)

    if white_count + blue_count == 1:
        return white_count, blue_count

    new_length = length//2

    paper1 = get_new_paper(paper, (0, 0), (new_length, new_length))
    new_white_count, new_blue_count = count_paper(paper1, new_length)
    white_count += new_white_count
    blue_count += new_blue_count

    paper2 = get_new_paper(paper, (new_length, 0), (length, new_length))
    new_white_count, new_blue_count = count_paper(paper2, new_length)
    white_count += new_white_count
    blue_count += new_blue_count

    paper3 = get_new_paper(paper, (0, new_length), (new_length, length))
    new_white_count, new_blue_count = count_paper(paper3, new_length)
    white_count += new_white_count
    blue_count += new_blue_count

    paper4 = get_new_paper(paper, (new_length, new_length), (length, length))
    new_white_count, new_blue_count = count_paper(paper4, new_length)
    white_count += new_white_count
    blue_count += new_blue_count

    return white_count, blue_count


length = int(sys.stdin.readline())

paper = [[] for _ in range(length)]


for row in range(length):
    paper[row].extend(map(int, sys.stdin.readline().rstrip().split()))


sys.setrecursionlimit(10**6)
print(*count_paper(paper, length), sep="\n")


