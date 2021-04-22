n = int(input())
scv = list(map(int, input().split()))
scv = scv + [0]*(3-len(scv))
scv.sort(reverse=True) 
### 정렬시키는 이유 ###
# 입력이 2 60 59일 때
# a 부터 차례로 줄여가므로 
# 0 51 53 같은 곳을 cnt가 많이 듦에도 먼저 방문해버리기 때문에
# 뒤에 b-9 차례에서 이미 방문한 곳이라 판단하고 지나쳐버린다.
result = float('inf')
dp = [[[-1]*61 for _ in range(61)] for _ in range(61)]

def sol(cnt,a,b,c):
    global result

    if cnt >= result:
        return

    a = a if a > 0 else 0
    b = b if b > 0 else 0
    c = c if c > 0 else 0

    if a==0 and b==0 and c==0:
        result = min(result, cnt)
        return
    
    if dp[a][b][c] == -1:
        dp[a][b][c] = 1
    else:
        return

    sol(cnt+1,a-9,b-3,c-1)
    sol(cnt+1,a-9,b-1,c-3)
    sol(cnt+1,a-3,b-9,c-1)
    sol(cnt+1,a-3,b-1,c-9)
    sol(cnt+1,a-1,b-9,c-3)
    sol(cnt+1,a-1,b-3,c-9)

sol(0,scv[0],scv[1],scv[2])

print(result)