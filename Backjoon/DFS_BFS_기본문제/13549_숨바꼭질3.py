from collections import deque

n, k = map(int, input().split())
# -1을 최소 방문 시간으로 한 이유는 
# 시작 방문 시간이 0이어서 0을 기준으로 해두면 
# +1 -1하다가 다시 재방문 할 수 있기 때문에
# -1로 초기 방문시간으로 지정
visit = [-1] * 100001
q = deque()
q.append(n)
# 최소 방문 시간
visit[n] = 0

while q:
    now_n= q.popleft()

    for i in (now_n+1, now_n-1, now_n*2):
        if 0 <= i and i < 100001:
            if visit[i] == -1: # 처음 방문
                if i != now_n*2:
                    visit[i] = visit[now_n]+1
                else:
                    visit[i] = visit[now_n]
                q.append(i)
            else:
                if i != now_n*2:
                    visit[i] = min(visit[i], visit[now_n]+1)
                else:
                    visit[i] = min(visit[i], visit[now_n])

print(visit[k])
