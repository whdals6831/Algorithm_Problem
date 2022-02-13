import sys

n = int(input())
apart = []
visit = [[False]*n for _ in range(n)]
x = [1,0,-1,0]
y = [0,1,0,-1]
apart_complex = []

def find_apart(apart, i, j):
    global apart_complex
    global visit

    if visit[i][j]:
        return

    visit[i][j] = True

    for k in range(4):
        if i+x[k]>=0 and i+x[k]<len(apart) and j+y[k]>=0 and j+y[k]<len(apart):
            if apart[i+x[k]][j+y[k]]=='1' and not visit[i+x[k]][j+y[k]]:
                apart_complex[-1] += 1
                find_apart(apart, i+x[k], j+y[k])
            else:
                visit[i+x[k]][j+y[k]] = True

for _ in range(n):
    apart.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(n):
        if apart[i][j] == '1' and not visit[i][j]:
            apart_complex.append(1)
            find_apart(apart, i, j)

apart_complex.sort()

print(len(apart_complex))
for i in apart_complex:
    print(i)