import sys
import math

n = int(input())
m = int(input())

city = [[float('inf')]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    if math.isinf(city[start][end]):
        city[start][end] = cost
    else:
        city[start][end] = min(city[start][end], cost)

start_city, end_city = map(int, input().split())

n = start_city
city[n][n] = 0

while True:
    visit[n] = 1
    now = n
    isNext = False
    min_cost = float('inf')

    for idx, cost in enumerate(city[n]):
        city[idx][idx] = min(city[now][now]+cost, city[idx][idx])
        if city[idx][idx] < min_cost and visit[idx] != 1:
            isNext = True
            n = idx
            min_cost = city[idx][idx]
    
    if not isNext:
        if 0 in visit[1:]:
            for i in visit[1:]:
                if visit[i] == 0:
                    if min_cost > city[i][i]:
                        min_cost = city[i][i]
                        n = i
        else:
            break
    
print(city[end_city][end_city])