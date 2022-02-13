import sys

# state
# 1.가로 2.대각선 3.세로
def pipe_move_dfs(x, y, state):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return
    
    if state == 1:
        if y+1 <= n-1 and house[x][y+1] == 0:
            pipe_move_dfs(x, y+1, 1)

        if x+1 <= n-1 and y+1 <= n-1 and house[x][y+1] == 0 and house[x+1][y+1] == 0 and house[x+1][y] == 0:
            pipe_move_dfs(x+1, y+1, 2)
    elif state == 2:
        if y+1 <= n-1 and house[x][y+1] == 0:
            pipe_move_dfs(x, y+1, 1)

        if x+1 <= n-1 and house[x+1][y] == 0:
            pipe_move_dfs(x+1, y, 3)

        if x+1 <= n-1 and y+1 <= n-1 and house[x][y+1] == 0 and house[x+1][y+1] == 0 and house[x+1][y] == 0:
            pipe_move_dfs(x+1, y+1, 2)
    elif state == 3:
        if x+1 <= n-1 and house[x+1][y] == 0:
            pipe_move_dfs(x+1, y, 3)

        if x+1 <= n-1 and y+1 <= n-1 and house[x][y+1] == 0 and house[x+1][y+1] == 0 and house[x+1][y] == 0:
            pipe_move_dfs(x+1, y+1, 2)

n = int(input())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
if house[n-1][n-1] == 1:
    print(answer)
else:    
    pipe_move_dfs(0,1,1)
    print(answer)