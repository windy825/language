# 1. 혼잡을 피하기 위해 하나의 출입구씩 선택하여 순차적으로 입장 할 수 있다.

# 2. 출입구가 선택되면, 해당 출입구에 대기하고 있는 낚시꾼들은 자신의 위치에서 가장 가까운 빈 낚시터 자리로 한 명씩 이동하여 차례대로 자리를 잡는다.
#   - 출입구에서 바로 위쪽의 낚시터까지의 거리는 1m 이며, 좌우로 한 칸씩 멀어질 때 마다 추가로 1m씩 멀어진다.
#   - 예를 들어 [Fig. 1]의 Gate1에서 4번 자리까지는 1m 이고, 3번과 5번자리는 2m의 거리가 된다.

# 3. 해당 출입구의 맨 마지막 사람의 경우, 가장 가까운 빈 자리가 두 곳이라면 하나를 선택해야 한다.
#    (맨 마지막 사람이 아닌 경우, 두 곳 중 아무데나 가도 결과는 같으므로 고려할 필요가 없다.)

# 4. 해당 출입구에 대기중인 모든 낚시꾼들의 자리잡기가 완료되면, 다음 출입구를 선택하여 위 1~3 과정을 반복 수행한다.

 

# 낚시터 자리의 개수 N이 주어지고, 출입구 3개의 위치 및 해당 출입구에 대기중인 각각의 낚시꾼들의 숫자가 주어진다.
# 이때 위의 낚시터 자리잡기 절차를 수행하면서 낚시꾼들 각각의 이동거리를 모두 더한 값이 최소가 되도록 자리잡는 방법을 찾고, 그때의 이동거리의 합을 출력하라.




from itertools import permutations


def check(where, distance, visit):
    global answer

    if distance >= answer:
        return

    if where == 3:
        if distance < answer:
            answer = distance
        return 

    gate, mans = case[line[where]-1]
    gate -= 1
    cnt = 0

    possible_line = [[i,abs(gate-i)+1] for i in range(n) if not visit[i]]  # 하나씩 분배하며 인원을 배치하기보단, 
    possible_line.sort(key=lambda x : x[1])                                # 가능한 우선순위를 지정해주었다(최소이동거리 기준 오름차순)

    target = 0
    while mans != 1:
        visit[possible_line[target][0]] = 1
        cnt += possible_line[target][1]
        mans -= 1
        target += 1
    
    if len(possible_line) >1 and possible_line[target][1] == possible_line[target+1][1]: # 만약에 이동거리가 같은 후보가 2개라면, 둘다 한번씩 가보는
        visit[possible_line[target][0]] = 1                                              # back tracking 으로 진행하고
        check(where +1, distance + cnt + possible_line[target][1], visit[::])
        visit[possible_line[target][0]] = 0
        visit[possible_line[target+1][0]] = 1
        check(where +1, distance + cnt + possible_line[target+1][1], visit[::])
        visit[possible_line[target+1][0]] = 0
 
    else:                                            # 후보가 다행히 하나라면, 그냥 그거 하나만 진행한다.
        visit[possible_line[target][0]] = 1
        check(where +1, distance + cnt + possible_line[target][1], visit[::])


tc = int(input())
for t in range(tc):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(3)] # 출입구 하나 1 빼야함
    
    answer = 3600

    for line in permutations(range(1,4), 3):
        check(0, 0, [0] * n)
    
    print(f'#{t+1} {answer}')