import sys
from sys import setrecursionlimit
setrecursionlimit(10**4+1)

n, m = map(int, input().split())
dp = [[-1]*1001 for _ in range(1001)]
len_names = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

def dfs(idx, cur_leng):
    if idx == n:
        return 0

    result = dp[idx][cur_leng]

    if result != -1:
        return result

    result = (m-cur_leng+1) * (m-cur_leng+1) + dfs(idx+1, len_names[idx]+1)

    if cur_leng+len_names[idx] <= m:
        result = min(result, dfs(idx+1, cur_leng+len_names[idx]+1))
    
    return result

print(dfs(1, len_names[0]+1)) # 새로 시작하는 열의 첫번째 값은 미리 더해주기 