case = [int(input()) for _ in range(9)]
total = sum(case)

for i in range(0, 9):
    for j in range(1, 9):
        if total - case[i] - case[j] == 100:
            answer = [num for num in case if num not in [case[i], case[j]]]
            print(*sorted(answer), sep='\n')
            quit()


# 9명중에 7명의 합이 100이라고 함.
# 그럼 9명의 합에서 2명을 뺀 수가 100이라면 요구조건에 맞는 답
# 2명을 뽑아내는 반복문을 시작하고, 조건문에서 그 2명을 뺐을때, 남은 7명의 합이
# 100이라면 답으로 뽑아내자