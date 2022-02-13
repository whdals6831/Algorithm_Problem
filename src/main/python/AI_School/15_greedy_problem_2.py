import sys

input = sys.stdin.readline

N, B = map(int, input().split())

coins = []
remain_coin_cnt = 0

for _ in range(N) :
    coins.append(int(input()))



# 반복문 방법
# for value in coins[::-1] :
#     remain_coin_cnt += B//value
#     B %= value

# print(remain_coin_cnt)



# 재귀 방법
def calc_minimum_cnt(before_money, now_idx, coins_list) :
    if before_money == 0 :
        return 0

    divisor, mod = divmod(before_money, coins_list[now_idx])

    return calc_minimum_cnt(mod, now_idx-1, coins_list) + divisor

print(calc_minimum_cnt(B, len(coins)-1,coins))