n = int(input()) # 객차의 수
train = list(map(int, input().split()))
sum_train = [0]*(n+1)
carryAble = int(input())

dp = [[0]*(n+1) for _ in range(4)] # 기관차가 1대, 2대 3대 각각 나눠서 메모이제이션

for i in range(1,n+1): # 누적 합
    sum_train[i] = sum_train[i-1] + train[i-1]

c = carryAble

for i in range(1,4):
    for j in range(c,n+1):
        # 점화식
        # 전 객차에서의 최대 손님값(dp[i][j-1])과
        # 현재 기관차에서 한대 줄어든 기관차에서 [현재 객차 - carryAble]위치의 손님값(dp[i-1][j-carryAble]) + 현재 끌 수 있는 객차의 손님값(sum_train[j]-sum_train[j-carryAble]) 
        # 중에서 최대값을 찾아 dp에 저장
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-carryAble]+sum_train[j]-sum_train[j-carryAble])
    c += carryAble

# print(sum_train)
# print(*dp, sep='\n')
print(dp[3][n])