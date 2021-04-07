from collections import deque

n, k = map(int, input().split())
# -1을 최소 방문 시간으로 한 이유는 
# 시작 방문 시간이 0이어서 0을 기준으로 해두면 
# +1 -1하다가 다시 재방문 할 수 있기 때문에
# -1로 초기 방문시간으로 지정
visit = [[-1, ""] for _ in range(100001)]
q = deque()
q.append(n)
# 최소 방문 시간
visit[n][0] = 0
# 최소 방문 시간대에 방문한 이동 경로 dict
# dictionary로 직전경로만 저장해서 다시 재구성하는 것이 
# 메모리도 아끼고 속도도 더 빠르다.
before = {}
before[n] = -1

while q:
    now_n= q.popleft()

    for i in (now_n+1, now_n-1, now_n*2):
        if 0 <= i and i < 100001:
            if visit[i][0] == -1: # 처음 방문
                visit[i][0] = visit[now_n][0]+1
                before[i] = now_n # 현재 경로에 바로 직전 경로 저장
                q.append(i)
        
# 경로 재구성 하기
i = k
answer = [k]

while before[i] != -1:
    answer.append(before[i])
    i = before[i]

answer.reverse()

print(visit[k][0])
print(" ".join(list(map(str, answer))))
