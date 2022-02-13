from collections import deque

n, m, k = map(int, input().split())
passage = [[0]*(m+2) for _ in range(n+2)]
visit = [[False]*(m+2) for _ in range(n+2)]
x = [1,0,-1,0]
y = [0,1,0,-1]
big_garbage = 0

for _ in range(k):
    r, c = map(int, input().split())
    passage[r][c] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if not visit[i][j] and passage[i][j] == 1:
            q = deque()
            q.append([i,j])
            visit[i][j] = True
            temp_garbage = 1

            while q:
                r, c = q.popleft()
                
                for k in range(4):
                    if passage[r+x[k]][c+y[k]] == 1 and not visit[r+x[k]][c+y[k]]:
                        q.append([r+x[k],c+y[k]])
                        visit[r+x[k]][c+y[k]] = True
                        temp_garbage += 1
            
            big_garbage = max(big_garbage, temp_garbage)

print(big_garbage)
        