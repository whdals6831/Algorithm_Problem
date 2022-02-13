n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in coins:
    for j in range(i, k+1):
        if j-i >= 0: 
            # j-i를 함으로써 현재 코인과 현재 코인을 제외한 가격의 경우의 수를 더함
            dp[j] += dp[j-i]

print(dp[k])
