from collections import deque

n = int(input())
signal = list(input())
sort_signal = []
idx = 0
jump = n//5
visit = [[0]*(jump+2) for _ in range(7)]
answer = ''
pattern_table = [['-1']*50 for _ in range(50)]

# pattern table
pattern_table[13][7] = '0'
pattern_table[5][5] = '1'
pattern_table[11][11] = '2'
pattern_table[11][7] = '3'
pattern_table[9][7] = '4'
pattern_table[11][7] = '5'


# signal 2차원 배열로 만들어주기
sort_signal.append(['.']*(jump+2))
for _ in range(5):
    sort_signal.append(list('.' + ''.join(signal[idx:idx+jump]) + '.'))
    idx += jump
sort_signal.append(['.']*(jump+2))

# signal pattern 찾기
def bfs(x, y):
    global sort_signal
    global visit
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    block_cnt = 0
    max_num = 0

    while q:
        nx, ny = q.popleft()
        block_cnt += 1

        for i in range(4):
            if visit[nx+dx[i]][ny+dy[i]] == 0 and sort_signal[nx+dx[i]][ny+dy[i]] == '#':
                q.append([nx+dx[i], ny+dy[i]])
                visit[nx+dx[i]][ny+dy[i]] = visit[nx][ny] + 1

                if visit[nx+dx[i]][ny+dy[i]] > max_num:
                    max_num = visit[nx+dx[i]][ny+dy[i]]

    return block_cnt, max_num

for i in range(jump+2):
    if sort_signal[1][i] == "#" and visit[1][i] == 0:
        block_cnt, max_num = bfs(1, i)


print(*sort_signal, sep="\n")
print(*visit, sep='\n')