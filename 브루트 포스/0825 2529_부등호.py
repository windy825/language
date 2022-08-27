k = int(input())
line = input().split()


maxx, minn = 0, 0
target = list(range(10))
target_reversed = target[::-1]

case = [0] * (k+1)

visit = [0] * 10
for num in range(k+1):
    