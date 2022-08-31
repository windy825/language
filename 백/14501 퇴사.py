from itertools import combinations as com

n = int(input())
case = [list(map(int, input().split())) for _ in range(n)]
case2 = [[i]+case[i] for i in range(n) if i + case[i][0] <= n]

target = []
for i in range(1, len(case2)+1):
    target.extend(list(com(case2, i)))

target.sort(key= lambda x : -sum(item[2] for item in x))

for line in target:
    line = list(line)
    line.sort(key= lambda x : x[0])

    flag = 0
    for item_idx in range(1, len(line)):
        if sum(line[item_idx - 1][:2]) > line[item_idx][0]:
            flag = 1
            break
    if flag:
        continue

    print(sum(item[2] for item in line))
    break
else:
    print(0)