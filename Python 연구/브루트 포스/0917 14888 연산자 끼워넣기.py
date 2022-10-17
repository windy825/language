from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

now_opers = []
for oper_idx, oper_cnt in enumerate(opers):
    for _ in range(oper_cnt):
        now_opers.append(oper_idx)

target = set(list(permutations(now_opers, N-1)))

minn = 1000000000
maxx = -1000000000
for case in target:
    temp = numbers[0]
    i = 1
    for oper in case:
        if oper == 0:
            temp += numbers[i]
        elif oper ==  1:
            temp -= numbers[i]
        elif oper ==  2:
            temp *= numbers[i]
        elif oper ==  3:
            if temp < 0 and numbers[i] > 0:
                temp = - (-temp // numbers[i])
            elif temp > 0 and numbers[i] < 0:
                temp = - (temp // -numbers[i])
            else:
                temp //= numbers[i]
        i += 1
    if temp > maxx:
        maxx = temp
    if temp < minn:
        minn = temp

print(maxx, minn, sep='\n')