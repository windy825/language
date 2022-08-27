dir = [(-1,0), (1,0), (0,-1), (0,1)]
rev_dir = [1, 0, 3, 2, 4]

def who_first(dir): # 0:red 1:blue
    global red_position, blue_position
    
    red = red_position
    blue = blue_position
    
    if dir == 0:
        if red[1] == blue[1]:
            if red[0] < blue[0]:
                return 0
            else:
                return 1
    
    elif dir == 1:
        if red[1] == blue[1]:
            if red[0] < blue[0]:
                return 1
            else:
                return 0
    
    elif dir == 2:    
        if red[0] == blue[0]:
            if red[1] < blue[1]:
                return 0
            else:
                return 1
    
    elif dir == 3:    
         if red[0] == blue[0]:
            if red[1] < blue[1]:
                return 1
            else:
                return 0
    
    return 0


def main(case, play_cnt, prev, red_position, blue_position):
    global answer

    def move_red(dir_idx):
        nonlocal new_case, red_position2, visit
        global n, m

        nowa, nowb = red_position2
        da, db = dir[dir_idx]
        new_a, new_b = nowa + da, nowb + db
        cnt = 0

        while True:
            if 0 <= new_a < n and 0 <= new_b < m:
                
                if new_case[new_a][new_b] == 'O':
                    cnt += 1
                    new_case[nowa][nowb] = '.'
                    visit[0] = 1
                    return 1
                
                elif new_case[new_a][new_b] == '.':
                    cnt += 1
                    new_a += da
                    new_b += db
                
                elif new_case[new_a][new_b] in 'B#':
                    new_case[nowa][nowb] = '.'
                    new_case[new_a - da][new_b - db] = 'R'
                    red_position = [new_a - da, new_b - db]

                    return 1 if cnt else 0
            
            else:
                return 1 if cnt else 0

    def move_blue(dir_idx):
        nonlocal new_case, blue_position2 , visit
        global n, m

        nowa, nowb = blue_position2
        da, db = dir[dir_idx]
        new_a, new_b = nowa + da, nowb + db
        cnt = 0

        while True:
            if 0 <= new_a < n and 0 <= new_b < m:
                
                if new_case[new_a][new_b] == 'O':
                    cnt += 1
                    new_case[nowa][nowb] = '.'
                    visit[0] = 1
                    return 1
                
                elif new_case[new_a][new_b] == '.':
                    cnt += 1
                    new_a += da
                    new_b += db
                
                elif new_case[new_a][new_b] in '#R':
                    new_case[nowa][nowb] = '.'
                    new_case[new_a - da][new_b - db] = 'B'
                    blue_position = [new_a - da, new_b - db]
                    return 1 if cnt else 0
            
            else:
                return 1 if cnt else 0


    if play_cnt >= 11 or answer < play_cnt:
        return
    
    for dir_idx in range(4):
        new_case = [case[i][:] for i in range(n)]
        red_position2 = red_position
        blue_position2 = blue_position
        visit = [0, 0]
     
        if rev_dir[prev] == dir_idx:
            continue
        temp = who_first(dir_idx)
        
        real_move = 0
        if temp == 0:
            real_move += move_red(dir_idx)
            real_move += move_blue(dir_idx)
        else:
            real_move += move_blue(dir_idx)
            real_move += move_red(dir_idx)

        if not real_move:
            continue
        if visit == [1, 0]:
            if play_cnt + 1 < answer:
                answer = play_cnt + 1
            continue 
        elif visit == [1,1]:
            continue

        main(new_case, play_cnt + 1, dir_idx, red_position, blue_position)



answer = 11
n, m = map(int, input().split())
case = [list(input()) for _ in range(n)]

red_position = []
blue_position = []
final_goal = []
for i in range(n):
    for j in range(m):
        if case[i][j] == 'R':
            red_position = [i,j]
        elif case[i][j] == 'B':
            blue_position = [i,j]
        elif case[i][j] == 'O':
            final_goal = [i,j]

main(case, 0, 4, red_position, blue_position)

print(-1 if answer == 11 else answer)