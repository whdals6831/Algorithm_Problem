n, k = map(int, input().split())

MAX_VALUE = 100*100000+1
coins = []
min_cnt = [MAX_VALUE] * (k+1)
min_cnt[0] = 0

# used_cnt = [[0] * n for _ in range(k+1)]

for _ in range(n):
    coins.append(int(input()))

for i in range(1, k+1):
    for idx, coin in enumerate(coins):
        if i >= coin and min_cnt[i] > 1 + min_cnt[i-coin]:
            min_cnt[i] = 1 + min_cnt[i-coin]
            # used_cnt[i] = used_cnt[i-coin][:]
            # used_cnt[i][idx] += 1

if min_cnt[k] == MAX_VALUE:
    print("-1")
else:
    # print(used_cnt)
    # print(used_cnt[k])
    print(min_cnt[k])