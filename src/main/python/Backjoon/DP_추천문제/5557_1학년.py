n = int(input())
nums = list(map(int, input().split()))

# 각 숫자마다 이전의 결과에 덧셈,뺄셈의 결과를 집어넣어줄 배열 생성
dp = [[0]*(21) for _ in range(n)]
idx = 1
dp[idx][nums[0]] = 1 # 맨 처음 숫자 index cnt

for num in nums[:-1]:
    for i, v in enumerate(dp[idx-1]): # 이전 결과를 참조
        if v == 0:
            continue
        if i + num <= 20:
            dp[idx][i+num] += v
        
        if i - num >= 0:
            dp[idx][i-num] += v
        
    idx += 1

print(dp[n-1][nums[-1]])