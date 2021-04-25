from collections import deque

field = [['.']+list(input())+['.'] for _ in range(12)]
field = [['.']*8] + field + [['.']*8]
visit = [[False]*8 for _ in range(14)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
chain_cnt = 0
isChange = True

while isChange:
    # 4개이상 모인 뿌요 제거
    isChange = False

    for i in range(12, 0, -1):
        for j in range(1,7):
            if not visit[i][j] and field[i][j] != '.':
                q = deque()
                temp = []
                q.append([field[i][j],i,j])
                temp.append([i,j])
                visit[i][j] = True
                chain = 1

                # 한 color에 대해서 bfs 시작
                while q:
                    color, x, y = q.popleft()
                    
                    for k in range(4):
                        if not visit[x+dx[k]][y+dy[k]] and color == field[x+dx[k]][y+dy[k]]:
                            q.append([color, x+dx[k], y+dy[k]])
                            temp.append([x+dx[k], y+dy[k]])
                            visit[x+dx[k]][y+dy[k]] = True
                            chain += 1
                
                if chain >= 4:
                    isChange = True
                    for x, y in temp:
                        field[x][y] = '.'
    if isChange:
        chain_cnt += 1
    visit = [[False]*8 for _ in range(14)]

    # 남은 뿌요 아래로 내리기
    for i in range(1,7):
        temp = []
        for j in range(12, 0, -1):
            if field[j][i] != '.':
                temp.append(field[j][i])
                field[j][i] = '.'
        
        idx = 12
        for color in temp:
            field[idx][i] = color
            idx -= 1

print(chain_cnt)