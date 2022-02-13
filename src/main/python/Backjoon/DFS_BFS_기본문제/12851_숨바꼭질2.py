from collections import deque

n, k = map(int, input().split())
# -1을 최소 방문 시간으로 한 이유는 
# 시작 방문 시간이 0이어서 0을 기준으로 해두면 
# +1 -1하다가 다시 재방문 할 수 있기 때문에
# -1로 초기 방문시간으로 지정
visit = [[-1, 0] for _ in range(100001)]
q = deque()
q.append(n)
# 최소 방문 시간
visit[n][0] = 0
# 최소 방문 시간대에 방문한 방법의 수
visit[n][1] = 1

while q:
    now_n= q.popleft()

    for i in (now_n+1, now_n-1, now_n*2):
        if 0 <= i and i < 100001:
            if visit[i][0] == -1: # 처음 방문
                visit[i][0] = visit[now_n][0]+1
                visit[i][1] = visit[now_n][1]
                q.append(i)
            elif visit[now_n][0]+1 == visit[i][0]: # 이미 방문한 곳인데, 최소 방문 시간이 동일할 경우
                visit[i][1] += visit[now_n][1] # 전에 방문한 곳의 최소방법의 수를 더해줌
        
print(visit[k][0])
print(visit[k][1])
