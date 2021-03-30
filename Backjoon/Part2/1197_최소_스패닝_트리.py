import sys
from heapq import heappush, heappop

v, e = map(int, input().split())

e_info = [[] for _ in range(v+1)]
visit = [False for _ in range(v+1)]
answer = 0

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    # 서로 연결된걸 알기 위해 양쪽으로 넣어줌
    e_info[a].append([c,b])
    e_info[b].append([c,a])

heap = []
visit[1] = True

for w_v in e_info[1]:
    heappush(heap, w_v)

while heap:
    weight, vertex = heappop(heap)

    if not visit[vertex]:
        for weight_v in e_info[vertex]:
            heappush(heap, weight_v)
        visit[vertex] = True
        answer += weight

print(answer)