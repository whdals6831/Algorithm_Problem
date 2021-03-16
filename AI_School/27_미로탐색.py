from collections import deque

n, m = map(int, input().split())
maze_map = [[0] * (m+2)]
visit = [[0] * (m+1) for _ in range(n+1)]

for _ in range(n):
    maze_map.append([0] + list(map(int, input()))+[0])
maze_map.append([0] * (m+2))

# for line in maze_map:
#     print(line)

pos_calc = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

q = deque()
q.append([1,1])
visit[1][1] = 1

while len(q) > 0:
    now_row, now_col = q.popleft()

    for d_row, d_col in pos_calc:
        n_row = now_row + d_row
        n_col = now_col + d_col
        if maze_map[n_row][n_col] == 1 and visit[n_row][n_col] == 0:
            q.append([n_row, n_col])
            visit[n_row][n_col] = visit[now_row][now_col] + 1

print(visit[n][m])

