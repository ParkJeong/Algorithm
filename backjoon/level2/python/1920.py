candidate_cases = int(input())
candidates = sorted(list(map(int, input().split())))

target_cases = int(input())
origin_targets = list(map(int, input().split()))

sorted_targets = sorted(origin_targets)
targets_dict = dict()


c_idx = 0
c_len = len(candidates)
t_idx = 0
t_len = len(sorted_targets)

while t_idx < t_len and c_idx < c_len:
    if sorted_targets[t_idx] == candidates[c_idx]:
        targets_dict[sorted_targets[t_idx]] = 1
        t_idx += 1
    elif sorted_targets[t_idx] < candidates[c_idx]:
        targets_dict[sorted_targets[t_idx]] = 0
        t_idx += 1
    else:
        c_idx += 1

while t_idx < t_len:
    targets_dict[sorted_targets[t_idx]] = 0
    t_idx += 1

for key in origin_targets:
    print(targets_dict[key])
