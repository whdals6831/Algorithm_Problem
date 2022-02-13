# bfs + 이분탐색

from sys import stdin
from collections import deque

n, m = map(int, input().split())
connect_bridge = [[] for _ in range(n+1)]

# 도시의 연결여부와 무게제한
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    connect_bridge[a].append((b,c))
    connect_bridge[b].append((a,c))

start, end = map(int, stdin.readline().split())

# 통과할 수 있는 무게의 최솟값 / 최댓값
_min, _max = 1, 1000000000

def bfs(w):
    q = deque()
    q.append(start)
    visit = set()
    visit.add(start)

    while q:
        a = q.popleft()
        for b, c in connect_bridge[a]:
            if b not in visit and c >= w:
                visit.add(b)
                q.append(b)
    
    return True if end in visit else False

# 이분 탐색 
# 시작 도시부터 도착 도시까지 갈 수 있는 여부를 
# 이분탐색의 방법으로 계속 찾아감
result = _min
while _min <= _max:
    mid = (_min + _max) // 2

    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1

print(result)