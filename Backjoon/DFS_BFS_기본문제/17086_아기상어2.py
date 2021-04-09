# import sys
# from collections import deque

# n, m = map(int, input().split())
# x = [1,0,-1,0,1,1,-1,-1]
# y = [0,1,0,-1,1,-1,1,-1]
# field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# max_safe = 0

# def find_max_safe(a, b):
#     global max_safe, n, m
#     q = deque()
#     q.append([a,b,0])
#     visit = [[False]*m for _ in range(n)]
#     visit[a][b] = True

#     while q:
#         i, j, cnt = q.popleft()

#         # 아기 상어가 존재하지 않을 경우 -> 문제를 읽어보니 이 로직은 불필요함
#         if cnt+1 == max(n, m):
#             max_safe = cnt
#             return

#         if field[i][j] == 0:
#             for k in range(8):
#                 if i+x[k] >= 0 and j+y[k] >= 0 and i+x[k] < n and j+y[k] < m and not visit[i+x[k]][j+y[k]]:
#                     if field[i+x[k]][j+y[k]] == 0:
#                         q.append([i+x[k], j+y[k], cnt+1])
#                         visit[i+x[k]][j+y[k]] = True
#                     else:
#                         max_safe = max(max_safe, cnt+1)
#                         return

# for a in range(n):
#     for b in range(m):
#         find_max_safe(a, b)

# print(max_safe)



# 코드 개선
import sys
from collections import deque

n, m = map(int, input().split())
dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_safe = 0

def find_max_safe(a, b):
    global max_safe, n, m
    q = deque()
    q.append([a,b])
    visit = [[-1]*m for _ in range(n)]
    visit[a][b] = 0

    while q:
        i, j= q.popleft()
        
        for k in range(8):
            nx, ny = i+dx[k], j+dy[k]
            if nx<0 or ny<0 or nx>=n or ny>= m:
                continue

            if field[nx][ny] == 1:
                max_safe = max(max_safe, visit[i][j]+1)
                return

            if visit[nx][ny] == -1:
                q.append([nx, ny])
                visit[nx][ny] = visit[i][j]+1

for a in range(n):
    for b in range(m):
        if field[a][b] == 0:
            find_max_safe(a, b)

print(max_safe)