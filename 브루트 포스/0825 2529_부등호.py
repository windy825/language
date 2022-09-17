from itertools import permutations

k = int(input())
line = input().split()

per_cases = list(permutations(range(0, 10), k+1))
min, max = 0, 0

# min 구하기
flag = 0
for case in per_cases:
    if flag:
        break
    for num_idx in range(1, k+1):
        if line[num_idx-1] == '<' and case[num_idx-1] >= case[num_idx]:
            break
        elif line[num_idx-1] == '>' and case[num_idx-1] <= case[num_idx]:
            break
    else:
        min = ''.join(map(str, case))
        flag = 1

# max 구하기
flag = 0
for case_idx in range(len(per_cases)-1, -1, -1):
    case = per_cases[case_idx]
    if flag:
        break
    for num_idx in range(1, k+1):
        if line[num_idx-1] == '<' and case[num_idx-1] >= case[num_idx]:
            break
        elif line[num_idx-1] == '>' and case[num_idx-1] <= case[num_idx]:
            break
    else:
        max = ''.join(map(str, case))
        flag = 1

print(max, min, sep='\n')