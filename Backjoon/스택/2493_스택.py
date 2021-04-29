from collections import deque

n = int(input())
tower = list(map(int, input().split()))
listen_tower = [0]*n

q = deque()
q.append([tower[-1], n-1])

for i in range(len(tower)-2, -1, -1):
    while q:
        if q[-1][0] <= tower[i]:
            tower_n, idx = q.pop()
            listen_tower[idx] = i+1
        else:
            break
    q.append([tower[i], i])

print(*listen_tower, sep=' ')