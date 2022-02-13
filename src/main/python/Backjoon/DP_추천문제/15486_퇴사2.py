import sys

n = int(input())

ti = [0]*(n+1)
pi = [0]*(n+1)
profit = [0]*(n+1)
max_profit = 0

for i in range(1, n+1):
    ti[i], pi[i] = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    finish_day = i+ti[i]-1
    # 현재 날짜 전 까지의 최대 이익
    max_profit = max(max_profit, profit[i-1])
    
    if finish_day <= n:
        profit[finish_day] = max(profit[finish_day], max_profit+pi[i])
        
print(max(profit))
