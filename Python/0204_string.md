### 문자열 비교

```python
for i in range(1,int(input())+1):
    n,m = input(), input()
    print(f'#{i} {1 if n in m else 0}') 
```



### 회 문

```python
for idx in range(1,int(input())+1):
    n,m = map(int,input().split())
    case = [input() for _ in range(n)]  # 가로
    case2 = list(map(''.join,zip(*case)))  # 세로

    for i in range(n):
        for j in range(n-m+1):
            if case[i][j:j+m] in case[i][::-1]:  # 가로
                print(f'#{idx} {case[i][j:j+m]}')                
                break
            
            elif case2[i][j:j+m] in case2[i][::-1]:  # 세로
                print(f'#{idx} {case2[i][j:j+m]}')                
                break
```



### 글자수

```python
for idx in range(1,int(input())+1):
    n,m = input(), input()
    print(f'#{idx} {max(m.count(i) for i in n)}')
```
