import sys

possession_card_num = int(sys.stdin.readline())
possession_card_list = list(map(int, sys.stdin.readline().rstrip().split()))

candidate_num = int(sys.stdin.readline())
candidate_card_list = list(map(int, sys.stdin.readline().rstrip().split()))

results = dict()
for idx in range(candidate_num):
    results[candidate_card_list[idx]] = 0

for possesion_card in possession_card_list:
    if possesion_card in results.keys():
        results[possesion_card] += 1

result = ""
for candidate in candidate_card_list:
    result += str(results[candidate]) + " "
print(result[:-1])
