t = int(input())
n_list = []

for _ in range(t):
    n_list.append(int(input()))

n_path = [0]*10001
n_path[1] = 1
n_path[2] = 1

def only_two_three(n):
    remain_n = 0
    
    if n%2 == 0:
        mok = n//2
        remain_n += mok//3 + 1
    else:
        n = n-3
        mok = n//2
        remain_n += mok//3 + 1

    return remain_n

for i in range(2, 10001):
    n_path[i] = n_path[i-1]+only_two_three(i)

for i in n_list:
    print(n_path[i])

# dp를 적극 활용한 버전
# import sys
# input = sys.stdin.readline

# t = int(input())
# arr = [int(input()) for _ in range(t)]
# dp = [0] * (max(arr) + 1)
# dp[0] = 1
# for i in range(1, 4):
#     for j in range(i, len(dp)):
#         dp[j] += dp[j - i]
        

# for a in arr:
#     print(dp[a])