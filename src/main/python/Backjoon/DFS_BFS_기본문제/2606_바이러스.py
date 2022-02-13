from collections import deque

com = int(input())
com_pair = int(input())
visit = [False]*(com+1)
network = [[0]*(com+1) for _ in range(com+1)]
virus_com = 0

for _ in range(com_pair):
    a, b = map(int, input().split())
    network[a][b] = 1
    network[b][a] = 1

visit[1] = True
q = deque()
q.append(1)

while q:
    now_com = q.popleft()

    for i, v in enumerate(network[now_com]):
        if v == 1 and not visit[i]:
            visit[i] = True
            virus_com += 1
            q.append(i)

print(virus_com)
    