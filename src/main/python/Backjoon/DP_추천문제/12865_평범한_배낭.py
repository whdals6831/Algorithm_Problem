import sys

n, k = map(int, input().split())

dp = [ [0]*(k+1) for _ in range(n+1) ] # 0-1 knapsack을 위해 2차원 배열
bag = []
i = 1

for _ in range(n):
    bag.append(list(map(int, sys.stdin.readline().split())))

for w, v in bag:
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j] # 기존의 최대값을 넣어줌
        if j-w >= 0: # 가방에 넣을 수 있는 크기인지 확인
            # 현재 가치(v) + 현재 weight를 제외한 기존 weight의 최대값의 합과
            # 기존의 최대값을 비교 
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w]) 

    i += 1

print(dp[n][k])