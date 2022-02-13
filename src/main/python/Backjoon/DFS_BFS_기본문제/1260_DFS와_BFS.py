import sys
from collections import deque
from heapq import heappush, heappop
from copy import deepcopy

n, m, v = map(int, sys.stdin.readline().split())
table = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

# 연결되어 있는 번호 테이블 생성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    table[a].append(b)
    table[b].append(a)

# 작은 번호 먼저 뽑을 수 있게 정렬
for i in table:
    i.sort()

def DFS(v, table, visit):
    q = deque()
    q.append([v, table[v]])
    result = []

    while q:
        now = q.pop()

        if visit[now[0]]:
            continue
        else:
            visit[now[0]] = True

        result.append(str(now[0]))

        # stack이므로 작은 번호가 번저 방문 될 수 있게 뒤에서 부터 검색
        for i in range(len(now[1])-1,-1,-1):
            if not visit[now[1][i]]:
                q.append([now[1][i], table[now[1][i]]])

    return result

def BFS(v, table, visit):
    q = deque()
    q.append([v, table[v]])
    result = []

    while q:
        now = q.popleft()

        if visit[now[0]]:
            continue
        else:
            visit[now[0]] = True

        result.append(str(now[0]))

        for i in now[1]:
            if not visit[i]:
                q.append([i, table[i]])

    return result

print(" ".join(DFS(v, deepcopy(table), deepcopy(visit))))
print(" ".join(BFS(v, deepcopy(table), deepcopy(visit))))