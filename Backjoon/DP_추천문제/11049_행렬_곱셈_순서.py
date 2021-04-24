from sys import stdin

n = int(input())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

# ex) t의 최소값을 구하기 위해서 아래 순번으로 계산

#   A B C D E
# A 1 2 3 4 t
# B 0 - - - 1
# C 0 0 - - 2
# D 0 0 0 - 3
# E 0 0 0 0 4

# 1 = A + BCDE + 행렬곱 추가비용
# 2 = AB + CDE + 행렬곱 추가비용
# 3 = ABC + DE + 행렬곱 추가비용
# 4 = ABCD + E + 행렬곱 추가비용

for x in range(1,n):# 거리가 x인 것까지
    for i in range(n-x):# i부터 시작
        j=i+x
        dp[i][j]=float('inf')
        for k in range(i,j): # 두 행렬의 곱에서 나오는 추가비용계산해서 더해주기
            dp[i][j]=min(dp[i][j], dp[i][k]+dp[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1])
            # print(x,i,j,matrix[i][0],matrix[k][1],matrix[j][1])
            # print(*dp, sep='\n')

print(dp[0][-1])