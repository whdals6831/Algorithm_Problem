import sys
from collections import deque

n, m = map(int, input().split())
maze = [[0]*(m+2) for _ in range(n+2)]
maze_cnt = [[0]*(m+2) for _ in range(n+2)]
visit = [[False]*(m+2) for _ in range(n+2)]
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

for i in range(1, n+1):
    j = 1
    row = list(map(int, sys.stdin.readline().rstrip()))

    for k in row:
        maze[i][j] = k
        j += 1

q = deque()
maze_cnt[1][1] = 1
visit[1][1] = True
q.append([1,1])

while q:
    now_x, now_y = q.popleft()

    for i in range(4):
        if maze[now_x+x[i]][now_y+y[i]] == 1 and not visit[now_x+x[i]][now_y+y[i]]:
            q.append([now_x+x[i], now_y+y[i]])
            visit[now_x+x[i]][now_y+y[i]] = True
            maze_cnt[now_x+x[i]][now_y+y[i]] = maze_cnt[now_x][now_y] + 1

print(maze_cnt[n][m])