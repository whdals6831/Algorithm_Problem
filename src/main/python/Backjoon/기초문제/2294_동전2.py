import math

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [float('inf') for _ in range(k+1)]
dp[0] = 0

for i in coins:
    for j in range(i, k+1):
            dp[j] = min(dp[j], dp[j-i]+1)

if math.isinf(dp[k]):
    print(-1)
else:
    print(dp[k])