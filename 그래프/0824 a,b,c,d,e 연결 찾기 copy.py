# 사람의 수 N      (5 ≤ N ≤ 2000) 
# 친구 관계의 수 M (1 ≤ M ≤ 2000) 
# 0 ≤ a
# b ≤ N-1
# a ≠ b

n, m = map(int, input().split())
visit = [0] * n
# dfs로 요구하는 5인관계(a>b>c>d>E) 체크하기
def dfs(num, length):
    global visit, case, answer
    if length == 4:
        answer = 1
        return 
    
    for i in case[num]:
        if not visit[i]:
            visit[i] = 1
            dfs(i, length + 1)
            visit[i] = 0
    return



# 인접 리스트
case = [[] for _ in range(n)]
answer = 0
for _ in range(m):
    a,b = map(int, input().split())
    case[a].append(b)
    case[b].append(a)

for i in range(n):
    if answer == 1:
        print(1)
        break
    visit[i] = 1
    dfs(i, 0)
    visit[i] = 0
else:
    print(0)