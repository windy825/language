from itertools import permutations

def check(per):
    global monster_visit, clients_visit, answer, total

    for position in per:
        if position < total: # monsters
            monster_visit[position] = 1
        else:
            if not monster_visit[position - total]:
                return

    line = [[0,0]]
    for i in per:
        if i < total:
            line.append(monsters[i][1])
        else:
            line.append(clients[i-total][1])
    total_time = sum([abs(line[i][0] - line[i-1][0]) + abs(line[i][1] - line[i-1][1]) for i in range(1, total*2+1)])

    if total_time < answer:
        answer = total_time
    return



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]

    monsters = []
    clients = []

    for i in range(n):
        for j in range(n):
            if case[i][j] > 0:  # 몬스터
                monsters.append([case[i][j], [i,j]])
            if case[i][j] < 0:  # 고객
                clients.append([case[i][j], [i,j]])
    
    monsters.sort(key=lambda x : x[0])
    clients.sort(key=lambda x : -x[0])
    total = len(monsters)
    answer = 10001

    for per in permutations(range(total*2), total*2):
        monster_visit = [0] * total
        check(per)

    print(f'#{tc} {answer}')
