import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
war_field = [['0']*(n+2) for _ in range(m+2)]
visit = [[False]*(n+2) for _ in range(m+2)]

for i in range(1, m+1):
    soldiers = list(sys.stdin.readline().rstrip())
    for j in range(1, n+1):
        war_field[i][j] = soldiers[j-1]

x = [1, 0 ,-1, 0]
y = [0, 1, 0, -1]

w_power = 0
b_power = 0

for a in range(1, m+1):
    for b in range(1, n+1):
        if visit[a][b]:
            continue

        now_soldier = war_field[a][b]
        soldier_cnt = 0
        q = deque()
        q.append([a, b])
        visit[a][b] = True
        
        # DFS
        while q:
            i, j = q.popleft()
            soldier_cnt += 1
            
            for k in range(4):
                if war_field[i+x[k]][j+y[k]] == now_soldier and not visit[i+x[k]][j+y[k]]:
                    visit[i+x[k]][j+y[k]] = True
                    q.append([i+x[k],j+y[k]])
        
        if now_soldier == 'W':
            w_power += soldier_cnt**2
        else:
            b_power += soldier_cnt**2

print(w_power, b_power)