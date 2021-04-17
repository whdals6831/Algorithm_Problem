# import sys
# sys.setrecursionlimit(1000000)

# n, m = map(int, input().split())
# dp = [[-1]*(m+1) for _ in range(n)]
# len_names = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# def dfs(idx, cur_leng):
#     if idx == n:
#         return 0

#     result = dp[idx][cur_leng]

#     if result != -1:
#         return result

#     result = (m-cur_leng+1) * (m-cur_leng+1) + dfs(idx+1, len_names[idx]+1)

#     if cur_leng+len_names[idx] <= m:
#         result = min(result, dfs(idx+1, cur_leng+len_names[idx]+1))
    
#     return result

# print(dfs(1, len_names[0]+1)) # 새로 시작하는 열의 첫번째 값은 미리 더해주기 

# 위의 코드는 로직은 맞지만 시간 초과가 남

import sys
sys.setrecursionlimit(100000)
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
arr = [int(read()) for _ in range(n)]
dp = [[-1] * (m+1) for _ in range(n)] # 메모이제이션

def solution(idx, remain_len):
    if idx == n-1: 
        return 0

    if remain_len > arr[idx+1]: # 현재 집어 넣을 수 있는 공간이 있을 때
        if dp[idx+1][remain_len-arr[idx+1]-1] != -1: # 현재 행에 넣는 경우 (이름 사이의 공백때문에 -1 추가)
            t1 = dp[idx+1][remain_len-arr[idx+1]-1]  
        else:
            t1 = solution(idx+1, remain_len-arr[idx+1]-1)

        if dp[idx+1][m-arr[idx+1]] != -1: # 다음 행으로 넘기는 경우
            t2 = dp[idx+1][m-arr[idx+1]] + remain_len*remain_len 
        else:
            t2 = solution(idx+1, m-arr[idx+1]) + remain_len*remain_len

        dp[idx][remain_len] = min(t1, t2)
    else: # 현재 집어 넣을 수 있는 공간이 없을 때
        if dp[idx+1][m-arr[idx+1]] != -1: # 다음 행으로 넘김
            dp[idx][remain_len] = dp[idx+1][m-arr[idx+1]] + remain_len*remain_len  
        else:
            dp[idx][remain_len] = solution(idx+1, m-arr[idx+1]) + remain_len*remain_len

    return dp[idx][remain_len]

print(solution(0, m-arr[0]))