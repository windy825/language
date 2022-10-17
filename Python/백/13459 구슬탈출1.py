dir = [[-1,0], [1,0], [0,-1], [0,1]]

n, m = map(int, input().split())
case = [list(input()) for _ in range(n)]

red, blue = [], []
for i in range(n):
    for j in range(m):
        if case[i][j] == 'R':
            red = [i, j]
        elif case[i][j] == 'B':
            blue = [i, j]

# 공 옮기기
def move_ball(ball, color):
    global goal_in

    nowa, nowb = ball
    while True:
        nowa += da
        nowb += db
        if 0 <= nowa < n and 0 <= nowb < m:
            if case[nowa][nowb] == '#':
                return [nowa - da, nowb - db]
            
            elif case[nowa][nowb] == 'O':
                if color == 'R':
                    goal_in[0] = 1
                else:
                    goal_in[1] = 1
                return [nowa, nowb]
        else:
            return [nowa - da, nowb - db]
# 우선순위 체크
def check(da, db):
    ra, rb = now_red
    ba, bb = now_blue

    if [da, db] == dir[0]:
        if rb == bb:
            if ra < ba:
                return 'R'
            else:
                return 'B'
    elif [da, db] == dir[1]:
        if rb == bb:
            if ra > ba:
                return 'R'
            else:
                return 'B'
    elif [da, db] == dir[2]:
        if ra == ba:
            if rb < bb:
                return 'R'
            else:
                return 'B'
    elif [da, db] == dir[3]:
        if ra == ba:
            if rb > bb:
                return 'R'
            else:
                return 'B'
    
    return 'anything'

# bfs
visit = [[red, blue]]
q = [[red, blue, 0]]

q_idx = 0
while q_idx != len(q):
    now_red, now_blue, cnt = q[q_idx]
    q_idx += 1

    if cnt >= 10:
        continue

    for da, db in dir:
        goal_in = [0, 0]
        new_red = move_ball(now_red, 'R')
        new_blue = move_ball(now_blue, 'B')
        
        if goal_in == [1,0] and cnt+1 <= 10:
            print(1)
            quit()
        elif goal_in == [0,0]:
            pass
        else:
            continue
        
        if new_red == new_blue:
            who_first = check(da, db)
            if who_first == 'R':
                new_blue = [new_red[0] - da, new_red[1] - db]
            elif who_first == 'B':
                new_red = [new_blue[0] - da, new_blue[1] - db]
        new_position = [new_red, new_blue]

        if new_position not in visit:
            visit.append(new_position)
            q.append(new_position + [cnt+1])
    

print(0)