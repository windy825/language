# n X n 크기에 여러 색의 사탕이 들어있음
# 딱 한번, 인접한 위치끼리 사탕 자리 바꾸기 가능
# 그상태에서, 행 또는 열 중에 같은 색의 사탕이 가장 많이 이어져 있는 갯수
# 그냥 일일히 다 구하자



# 2. 자리바꾼 상태에서 다 체크해보기
def maxChange(case):
    global answer, n
    
    for i in range(n):
        temp = 1
        for j in range(1, n):
            if case[i][j] == case[i][j-1]:
                temp += 1
            else:
                if temp > answer:
                    answer = temp
                temp = 1
        if temp > answer:
            answer = temp
    



# 1. 사탕 자리 바꾸기
n = int(input())
case = [list(input()) for _ in range(n)]

answer = 1
for i in range(0, n):
    for j in range(0, n-1):
        case[i][j], case[i][j+1] = case[i][j+1], case[i][j]
        maxChange(case)
        maxChange(list(zip(*case)))
        case[i][j], case[i][j+1] = case[i][j+1], case[i][j]
        if answer == n:
            print(n)
            quit()

        case[j][i], case[j+1][i] = case[j+1][i], case[j][i]
        maxChange(case)
        maxChange(list(zip(*case)))
        case[j][i], case[j+1][i] = case[j+1][i], case[j][i]
        if answer == n:
            print(n)
            quit()

print(answer)