dir = [(-1,0), (1,0), (0,-1), (0,1)]

def check(da, db, red, blue):
    if (da, db) == (-1, 0):
        if red[1] == blue[1]:
            if red[0] > blue[0]:
                return 0
            else:
                return 1
    elif (da, db) == (1, 0):
        if red[1] == blue[1]:
            if red[0] > blue[0]:
                return 1
            else:
                return 0
    elif (da, db) == (0, -1):
        if red[0] == blue[0]:
            if red[1] < blue[1]:
                return 1
            else:
                return 0
    elif (da, db) == (0, 1):
          if red[0] == blue[0]:
            if red[1] < blue[1]:
                return 0
            else:
                return 1
    return -1

def move(ball_position, da, db, color):
    global goal_visit

    now_a, now_b = ball_position
    while True:
        now_a += da
        now_b += db

        if case[now_a][now_b] == '#':
            return [now_a - da, now_b - db]
        
        elif case[now_a][now_b] == 'O':
            if color == 'R':
                goal_visit[0] = 1
            else:
                goal_visit[1] = 1
            return [now_a, now_b]

n, m = map(int, input().split())
case = [list(input()) for _ in range(n)]

red_position = []
blue_position = []
for i in range(n):
    for j in range(m):
        if case[i][j] == 'R':
            red_position = [i, j]
        elif case[i][j] == 'B':
            blue_position = [i, j]
        
answer = -1
balls_visit = [[red_position, blue_position]]
goal_visit = [0,0]

q = [[red_position, blue_position, 0]]
idxing = 0
while idxing != len(q):
    now_red, now_blue, cnt = q[idxing]
    idxing +=1

    if cnt > 10:
        continue

    for da, db in dir:
        temp_position = []
        who_first = check(da,db, now_red, now_blue)

        temp_red = move(now_red, da, db, 'R')
        temp_blue = move(now_blue, da, db, 'B')

        if temp_red == temp_blue:
            if who_first == 1: # red
                temp_position = [temp_red, [temp_red[0] - da, temp_red[1] - db]]
            elif who_first == 0: # blue
                temp_position = [[temp_blue[0] - da, temp_blue[1] - db], temp_blue]
        else: # 아무나
            temp_position = [temp_red, temp_blue]
        
        if goal_visit == [1, 0]:
            if cnt + 1 < 11:
                print(cnt + 1)
                quit()
            else:
                continue
        elif goal_visit != [0, 0]:
            goal_visit = [0, 0]
            continue

        if temp_position in balls_visit:
            continue
        else:
            balls_visit.append(temp_position)
            q.append([*temp_position, cnt + 1])

print(answer)